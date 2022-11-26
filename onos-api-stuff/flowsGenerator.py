import requests
from requests.auth import HTTPBasicAuth
import json

ipOnos = "http://192.168.1.20:8181/onos/v1/"
def connectionsUpload():
    r = requests.get(ipOnos + "links", auth=HTTPBasicAuth("onos", "rocks"))
    return r.json()["links"]
nodes = connectionsUpload()


def deviceAndHost():
    with open("deviceAndHost.json") as deviceAndHost:
        return json.load(deviceAndHost)
dAH = deviceAndHost()

def mainForm():
    # loading a form which was attached with task
    with open("trackForm.json") as trackForm:
        return json.load(trackForm)
form = mainForm()

connection_ports_dict = {}
def savePortsOfDevice(deviceId:str):
    for link in nodes:
        if link["src"]["device"] == deviceId:
            if deviceId not in connection_ports_dict:
                connection_ports_dict[deviceId] = {}

            # output of that device and input of second device
            connection_ports_dict[deviceId][link["dst"]["device"]] = {"OUT": link["src"]["port"], "IN": link["dst"]["port"]}

def netflowAdderFunction(deviceId:str, inputPort:str, outputPort:str, ipDest:str):
    form["deviceId"] = deviceId
    form["treatment"]["instructions"][0]["port"] = outputPort
    form["selector"]["criteria"][0]["port"] = inputPort
    form["selector"]["criteria"][2]["ip"] = ipDest
    adder = requests.post(ipOnos + "flows/" + deviceId, json=form, auth=HTTPBasicAuth("onos", "rocks"))

def initNetflow(mainPoints:tuple):

    dev1 = mainPoints[0]
    dev2 = mainPoints[-1]
    IP1 = dAH[dev1]
    IP2 = dAH[dev2]
    trackFlow = mainPoints[1:-1]
    savePortsOfDevice(dev1)
    savePortsOfDevice(dev2)

    if len(trackFlow) == 0:
        netflowAdderFunction(dev1, '1', connection_ports_dict[dev1][dev2]['OUT'], IP2)
        netflowAdderFunction(dev1, connection_ports_dict[dev1][dev2]['OUT'], '1', IP1)
        netflowAdderFunction(dev2, '1', connection_ports_dict[dev2][dev1]["OUT"], IP1)
        netflowAdderFunction(dev2, connection_ports_dict[dev2][dev1]['OUT'], '1', IP2)

    if len(trackFlow) > 0:
        onePoint = trackFlow[0]
        lastPoint = trackFlow[len(trackFlow) - 1]
        netflowAdderFunction(dev1, "1", connection_ports_dict[dev1][onePoint]['OUT'], IP2)
        netflowAdderFunction(dev1, connection_ports_dict[dev1][onePoint]['OUT'], "1", IP1)
        netflowAdderFunction(dev2, "1", connection_ports_dict[dev2][lastPoint]['OUT'], IP1)
        netflowAdderFunction(dev2, connection_ports_dict[dev2][lastPoint]['OUT'], "1", IP2)

        for dev in trackFlow:
            savePortsOfDevice(dev)
        for a in range(len(trackFlow)):
            dev = trackFlow[a]
            if dev == onePoint and dev == lastPoint:
                netflowAdderFunction(dev, connection_ports_dict[dev1][dev]['IN'],
                                     connection_ports_dict[dev][dev2]['OUT'], IP2)
                netflowAdderFunction(dev, connection_ports_dict[dev2][dev]['IN'],
                                     connection_ports_dict[dev][dev1]['OUT'], IP1)
                break
            if dev == onePoint:
                nextDevice = trackFlow[a+1]
                netflowAdderFunction(dev, connection_ports_dict[dev1][dev]['IN'],
                                     connection_ports_dict[dev][nextDevice]['OUT'], IP2)
                netflowAdderFunction(dev, connection_ports_dict[nextDevice][dev]['IN'],
                                     connection_ports_dict[dev][dev1]['OUT'], IP1)
            if dev == lastPoint:
                lastDevice = trackFlow[a-1]
                netflowAdderFunction(dev, connection_ports_dict[lastDevice][dev]['IN'],
                                     connection_ports_dict[dev][dev2]['OUT'], IP2)
                netflowAdderFunction(dev, connection_ports_dict[dev2][dev]['IN'],
                                     connection_ports_dict[dev][lastDevice]['OUT'], IP1)



