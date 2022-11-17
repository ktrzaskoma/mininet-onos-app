import requests
from requests.auth import HTTPBasicAuth
import json

onosIp = "http://172.20.10.5:8181/onos/v1/"


def getLinks():
    r = requests.get(onosIp+"links", auth=HTTPBasicAuth("onos", "rocks"))
    return r.json()["links"]

def getHosts():
    with open("deviceIDs.json") as file:
        return json.load(file)

def getTemplate():
    with open("form.json") as file:
        return json.load(file)

template = getTemplate()

hosts = getHosts()

links = getLinks()

ports = {}

def savePortsOfDevice(deviceId:str):
    for link in links:
        if link["src"]["device"] == deviceId:
            if deviceId not in ports:
                ports[deviceId] = {}

            # output of that device and input of second device
            ports[deviceId][link["dst"]["device"]] = {"output": link["src"]["port"], "input": link["dst"]["port"]}

def addFlow(deviceId:str, inputPort:str, outputPort:str, ipDest:str):
    template["deviceId"] = deviceId
    template["treatment"]["instructions"][0]["port"] = outputPort
    template["selector"]["criteria"][0]["port"] = inputPort
    template["selector"]["criteria"][2]["ip"] = ipDest

    r = requests.post(onosIp + "flows/" + deviceId, json=template, auth=HTTPBasicAuth("onos", "rocks"))

def createDirectFlow(nodes):

    device1 = nodes[0]
    device2 = nodes[-1]

    ip1 = hosts[device1]
    ip2 = hosts[device2]

    route = nodes[1:-1]

    savePortsOfDevice(device1)
    savePortsOfDevice(device2)

    if len(route) == 0:
        addFlow(device1, "1", ports[device1][device2]["output"], ip2)
        addFlow(device1, ports[device1][device2]["output"], "1", ip1)

        addFlow(device2, "1", ports[device2][device1]["output"], ip1)
        addFlow(device2, ports[device2][device1]["output"], "1", ip2)


    if len(route) > 0:

        firstStop = route[0]
        lastStop = route[len(route) - 1]

        addFlow(device1, "1", ports[device1][firstStop]["output"], ip2)
        addFlow(device1, ports[device1][firstStop]["output"], "1", ip1)

        addFlow(device2, "1", ports[device2][lastStop]["output"], ip1)
        addFlow(device2, ports[device2][lastStop]["output"], "1", ip2)

        for device in route:
            savePortsOfDevice(device)

        for i in range(len(route)):
            device = route[i]
            if device == firstStop and device == lastStop:
                addFlow(device, ports[device1][device]["input"], ports[device][device2]["output"], ip2)
                addFlow(device, ports[device2][device]["input"], ports[device][device1]["output"], ip1)
                break

            if device == firstStop:
                nextDevice = route[i+1]
                addFlow(device, ports[device1][device]["input"], ports[device][nextDevice]["output"], ip2)
                addFlow(device, ports[nextDevice][device]["input"], ports[device][device1]["output"], ip1)
            if device == lastStop:
                lastDevice = route[i-1]
                addFlow(device, ports[lastDevice][device]["input"], ports[device][device2]["output"], ip2)
                addFlow(device, ports[device2][device]["input"], ports[device][lastDevice]["output"], ip1)



createDirectFlow(("of:0000000000000001", "of:0000000000000003"))
