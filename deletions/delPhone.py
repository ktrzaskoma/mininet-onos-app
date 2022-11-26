import requests
from requests.auth import HTTPBasicAuth

onosIp = "http://172.20.10.5:8181/onos/v1/"

r = requests.delete(onosIp + "manual-flows-setting/application/org.onosproject.rest", auth=HTTPBasicAuth("onos","rocks"))

print(r.status_code)