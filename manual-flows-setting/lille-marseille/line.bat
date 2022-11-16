

curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:000000000000000a" -d @flow10.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:000000000000000a" -d @flow10_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000008" -d @flow8.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000008" -d @flow8_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000007" -d @flow7.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000007" -d @flow7_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000001" -d @flow1.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000001" -d @flow1_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000002" -d @flow2.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://172.20.10.5:8181/onos/v1/flows/of:0000000000000002" -d @flow2_.json -H "Content-Type: application/json" -H "Accept: application/json"
pause