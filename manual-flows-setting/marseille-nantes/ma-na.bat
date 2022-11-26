curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:000000000000000a" -d @flow10.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:000000000000000a" -d @flow10_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000009" -d @flow9.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000009" -d @flow9_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000006" -d @flow6.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000006" -d @flow6_.json -H "Content-Type: application/json" -H "Accept: application/json"

curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000004" -d @flow4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user onos:rocks -X POST "http://192.168.1.20:8181/onos/v1/flows/of:0000000000000004" -d @flow4_.json -H "Content-Type: application/json" -H "Accept: application/json"

pause