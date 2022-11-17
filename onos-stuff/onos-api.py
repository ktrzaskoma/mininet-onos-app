import json
from bottle import delete, post, request
import requests
from requests.auth import HTTPBasicAuth
from dijkstar import Graph, find_path
# from flow-generator import creatDirectFlows

onosIp = "http://172.20.10.5:8181/onos/v1"

def creatGraph():
    with open("links.json") as file:
        links = json.load(file)
        g = Graph()
        for link in links:
            g.add_edge()
            g.add_edge()
