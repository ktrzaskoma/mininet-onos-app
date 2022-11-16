import json
from bottle import delete, post, request
import requests
from requests.auth import HTTPBasicAuth
from dijkstar import Graph, find_path


Ip = "http://172.20.10.5:8181/onos/v1"
