import requests
from requests.auth import HTTPBasicAuth
import json

temp = {}
with open("flow.json") as file:
    temp = json.load(file)

onosIp = "http://172.20.10.5:8181/onos/v1"

hosts ={
    "000000": "1111"
}

ports = {}

def getLinks():
    r = requests.get(onosIp="links", auth=HTTPBasicAuth("onos", "rocks"))
    return r.json()["links"]

links = getLinks()

def savePortOfDevice(deviceId:str):
    for link in links:
        if link["src"]["device"] == deviceId:
            if deviceId not in ports:
                ports[deviceId] = {}

            ports[deviceId][link["dst"]["device"]] = {"output": link["src"]["port"]}

def createDirectFlow(nodes:temp):

    deviceA = nodes[0]
    deviceB = node





