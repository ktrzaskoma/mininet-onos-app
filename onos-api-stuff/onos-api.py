import json

import delete as delete
import requests
from bottle import post, run, request
from dijkstar import Graph, find_path
from requests.auth import HTTPBasicAuth
from flowsGenerator import initNetflow

ipOnos = "http://192.168.1.20:8181/onos/v1/"
# simple api with 2 requests, used bottle framework
def setUpDevices():
    with open("deviceAndHost.json") as file:
        return dict([(value, key) for key, value in json.load(file).items()])

def setUpDijkstraAlgorithm():
    with open("netflowsData.json") as file:
        links = json.load(file)
        g = Graph()
        for link in links:
            g.add_edge(link["from"], link["to"], link["delay"])
            g.add_edge(link["to"], link["from"], link["delay"])
        return g

# dictionary to store infos about devices ids and delays
netflowsData = {}
initGraph = setUpDijkstraAlgorithm()
initSwitches = setUpDevices()
# DELETE request to delete all netflows in cofigured in france-net topology
# @delete('/delete')
# def deleteNF():
#     delete = requests.delete(ipOnos + 'flows/application/org.onosproject.rest', auth=HTTPBasicAuth('onos', 'rocks'))
#     return str(delete.status_code)

# POST request to add netflows
@post('/add')
def addNF():
    dataNF = request.json
    # find_path is method from library dijkstar,
    # thanks to this it helps with looking for best path
    connectionPoints\
        = find_path(initGraph, initSwitches[dataNF['ip1'] + '/32'],
                    initSwitches[dataNF['ip2'] + '/32']).nodes
    excludedNetflows:list[str] = []

    for a in range(len(connectionPoints) - 1):
        if connectionPoints[a]+connectionPoints[a + 1] in netflowsData:
            if netflowsData[connectionPoints[a] + connectionPoints[a + 1]] > 100:
                excludedNetflows.append(connectionPoints[a] + connectionPoints[a + 1])

    if len(excludedNetflows) == 0:
        for b in range(len(connectionPoints) - 1):
            if connectionPoints[b] + connectionPoints[b + 1] in netflowsData:
                netflowsData[connectionPoints[b] + connectionPoints[b + 1]]\
                    = netflowsData[connectionPoints[b] + connectionPoints[b + 1]]
            if connectionPoints[b + 1] + connectionPoints[b] in netflowsData:
                netflowsData[connectionPoints[b + 1] + connectionPoints[b]]\
                    = netflowsData[connectionPoints[b + 1] + connectionPoints[b]]

    if(len(excludedNetflows) > 0):
        graph = setUpDijkstraAlgorithm()
        for flow in excludedNetflows:
            args = (flow[0:19], flow[19:])
            graph.remove_edge(*args)

        connectionPoints\
            = find_path(graph, initSwitches[dataNF['ip1']], initSwitches[dataNF['ip2']]).nodes
        for c in range(len(connectionPoints) - 1):
            if (connectionPoints[c] + connectionPoints[c + 1]) in netflowsData:
                netflowsData[connectionPoints[c] + connectionPoints[c + 1]]\
                    = netflowsData[connectionPoints[c] + connectionPoints[c + 1]]
            if connectionPoints[c + 1] + connectionPoints[c] in netflowsData:
                netflowsData[connectionPoints[c + 1] + connectionPoints[c]]\
                    = netflowsData[connectionPoints[c + 1] + connectionPoints[c]]
        initNetflow(tuple(connectionPoints))
    initNetflow(tuple(connectionPoints))

# special server to control operations on france-net topology
run(host="localhost", port=8080)
