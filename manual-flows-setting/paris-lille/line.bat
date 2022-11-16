
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000002" -d @flow2.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000002" -d @flow2_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000001" -d @flow1.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000001" -d @flow1_.json -H "Content-Type: application/json" -H "Accept: application/json"
pause