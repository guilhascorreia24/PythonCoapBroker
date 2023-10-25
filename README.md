# Efento Coap Server
## General description
This server was developed for the integration of efento devices and was in the context of the project TECSOS and CHB, this server has the functionalities of receive and send to thingworx the data, device informations and configurations from efento devices (waterLeak, motion, temperature & humidity).

The server is constantly listening for data sent by Efento NB-IoT sensors. Once a new message arrives, the server parses the data, saves it in the PostgreSQL database and responds to the sensor with confirmation that the message has been received (code  2.01 “CREATED”). This means that the message has been successfully parsed and saved in the database. If anything goes wrong (e.g. database is down), the sensor will receive a response with code 5.00 “INTERNAL_SERVER_ERROR” . In that case, the NB-IoT sensor will retry to send the same data after a while.

## Table of Contents


- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Procedure](#procedure)
  - [Example Message](#example-message)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)



## Getting Started

 

### Prerequisites

 

Before you begin, ensure you have met the following requirements:

 

- Python 3.9. You can download Python from [python.org](https://www.python.org/downloads/).
- Proto files used deserialise the data coming from the sensors. You can consult the files [here](https://github.com/efento/Proto-files)

 
## Procedure
Receive frames in Protobuf format  -> descrypher using Protobuf files for deserialize the data sent -> transmit this in type of json to thingworx and in type of Protobuf to device with an ACK 
### example type message
#### Measument Frame
This message are sent to the endpoint "/m"   
input: 
```txt
\n\x06(,\x02AV\xaf\x10\x01\x18\x14"\r\x08\x05\x10\xe0\xf7\xe1\xa7\x06*\x03\x01\xc1\x07(\xac\xff\xe1\xa7\x060\x148\x0c@\x01Hw\x82\x01\x00
```

output to thingworx:
```json
{"measurements": [{"measured_at": "2023-09-06 14:17:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:17:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:17:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:18:00 UTC", "signal": 0, "measurement_interval": 
20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:18:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:18:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:18:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:18:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:18:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:19:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:19:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:19:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:19:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:19:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:19:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:20:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:20:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:20:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": 
"ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:20:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:20:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:20:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:21:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", 
"params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:21:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:21:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:21:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:21:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:21:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:22:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:22:00 UTC", "serial": "282C024156AF", 
"next_measurement_at": "2023-09-06 14:22:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:22:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:22:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:22:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:23:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:23:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:23:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": 
"OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:23:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:23:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:23:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:24:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", 
"type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:24:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:24:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:24:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:24:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:24:40 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:25:00 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:25:00 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:25:20 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}, {"measured_at": "2023-09-06 14:25:20 UTC", "serial": "282C024156AF", "next_measurement_at": "2023-09-06 14:25:40 UTC", "signal": 0, "measurement_interval": 20, "batteryStatus": "ok", "params": [{"value": "OK", "type": "open-close", "channel": 1}]}]}
```

output to device:
```
\x98\x01\x01
```

#### Configuration Frame
This message are sent to the endpoint "/c"   
input: 
```txt
\x10\x1e\x18x \xff\xff\xff\xff\x0f(\xff\xff\xff\xff\x0fH\xff\xff\x03P\xff\xff\x03Z\x0e35.216.198.132`\xc8\x1fj\r18.184.24.239p\xd0\x86\x03x\xb0,\x82\x01\x01\x7f\x88\x01\xc0\x84=\xa2\x01\x03\x82\xa2\x01\xa8\x01\xcc\x01\xb8\x01\xff\x01\xc2\x01$00000000-0000-0000-0000-000000000000\xca\x01\x06(,\x02@\xfd4\xd0\x01\x01\xda\x01\x06\x01\x02\x00\x00\x00\x00\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe2\x01\x02\x10\x01\xe8\x01\xff\xff\xff\xff\x0f\xf8\x01\xff\xff\x03\x82\x02\x01m\x8a\x02\x01c\x92\x02\x01i\x9a\x02\x01t\xa0\x02\x01\xb0\x02\xf5\xee\xdd\xa3\x06\xb8\x02\xd0\xc2\xf6\xa3\x06\xc0\x02\xe8\xfb\x03\xc8\x02\xe8\xfb\x03\xd2\x02\x08\xff\x01\xff\x01\xff\x01\xff\x01\xd8\x02\x82\xde4\xe0\x02\x02\xf2\x02\x12\x08\x02\x01\x01\x02\x02\x0b\x01\x0b\xff\xff\x03\xff\xff\x03\xff\xff\x03\xfa\x02\x02\x18\x01\xfa\x02\x02\x18\x01\xfa\x02\x02\x18\x01\xfa\x02\x02\x18\x01\xfa\x02\x02\x18\x01\xfa\x02\x02\x18\x01
```

output to thingworx:
```json
{"measurementPeriodBase": 30, "transmissionInterval": 120, "bleTurnoffTime": 4294967295, "ackInterval": 4294967295, "transferLimit": 65535, "transferLimitTimer": 65535, "dataServerIp": "35.216.198.132", "dataServerPort": 4040, "updateServerIp": "18.184.24.239", "updateServerPortUdp": 50000, "updateServerPortCoap": 5680, "apn": "\u007f", "plmnSelection": 1000000, "errors": [20738], "hash": 204, "cloudTokenConfig": 255, "cloudToken": "00000000-0000-0000-0000-000000000000", "serialNumber": "282C0240FD34", "measurementPeriodFactor": 1, "channelTypes": ["MEASUREMENT_TYPE_TEMPERATURE", "MEASUREMENT_TYPE_HUMIDITY", "MEASUREMENT_TYPE_NO_SENSOR", "MEASUREMENT_TYPE_NO_SENSOR", "MEASUREMENT_TYPE_NO_SENSOR", "MEASUREMENT_TYPE_NO_SENSOR"], "rules": [{"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}, {"condition": "CONDITION_DISABLED"}], "supervisionPeriod": 4294967295, "modemBandsMask": 65535, "dataEndpoint": "m", "configurationEndpoint": "c", "deviceInfoEndpoint": "i", "timeEndpoint": "t", "bleTxPowerLevel": 1, "errorTimestamp": 1685550965, "hashTimestamp": 1685954896, "cloudTokenCoapOption": 65000, "payloadSignatureCoapOption": 65000, "dnsServerIp": [255, 255, 255, 255], "dnsTtlConfig": 864002, "payloadSplitInfo": 1, "cellularConfigParams": [8, 2, 1, 1, 2, 2, 11, 1, 11, 65535, 65535, 65535], "calendars": [{"type": "CALENDAR_TYPE_DISABLED"}, {"type": "CALENDAR_TYPE_DISABLED"}, {"type": "CALENDAR_TYPE_DISABLED"}, {"type": "CALENDAR_TYPE_DISABLED"}, {"type": "CALENDAR_TYPE_DISABLED"}, {"type": "CALENDAR_TYPE_DISABLED"}]}
```
#### Device Information Frame
This message are sent to the endpoint "/i"   
input: 
```txt
\n\x06(,\x02AV\xaf\x18\x8a\x0cj\x1f\x08\xba\xe3\x9c\x02\x12\x07\xcb\xbc\x01\x00\xcb\xbc\x01\x18* \xf7\x1b(*0\x84\xe5\xc6\xa4\x0684@\x18r6\x08\x01\x122\xdca\x04\xa6\x05\xaa\x98\xd9D\xc9\x01\x0f\xbb\x01\x0c(\xbe\x0c\x00\xcc\x03\x04\x01\x01\x01\x00\x00\x00\x00\x00\xf6\x06\xbc\x02\x0e\n\x00\x00\x02\x00\x02\x00\xe0\xa1(\xd6\xae\x01\x84\x01z\x07040df20\x82\x01\x00\x8a\x018\x00\x8c\xdf\x80\xa4\x06\x90\xbf\x03\x8e \x00\x00n\x00\x00\x85\x04\x00\x00\x00\x00\x00\xb0\x80\xaa\xa2\x06\xa8\xde\x80\xa4\x06\x90\xe3\xfc\xa3\x06\xff\xff\xff\xff\x0f\xff\xff\xff\xff\x0f\xff\xff\xff\xff\x0f\x8c\x9f\x02\x92\x01\x08\x08\x93\xd8\xc4\xa4\x06\x10\x06
```

output to thingworx:
```json
{"serialNum": "KCwCQVav", "swVersion": 1546, "runtimeInfo": {"upTime": 4665786, "messageCounters": [24139, 0, 24139], "mcuTemperature": 21, "minBatteryVoltage": 3575, "minBatteryMcuTemperature": 21, 
"batteryResetTimestamp": 1687270020, "maxMcuTemperature": 26, "minMcuTemperature": 12}, "modem": {"type": "MODEM_TYPE_BC66", "parameters": [6254, 2, 339, 72033813, -101, -8, -94, 6, 20, 799, 0, 230, 2, -1, -1, -1, 0, 0, 0, 0, 0, 443, 158, 7, 5, 0, 0, 1, 0, 1, 0, 329840, 11179, 66]}, "commitId": "040df20", "memoryStatistics": [0, 1686122380, 57232, 4110, 0, 0, 110, 0, 0, 517, 
0, 0, 0, 0, 0, 1682604080, 1686122280, 1686057360, 4294967295, 4294967295, 4294967295, 36748], "lastUpdateInfo": {"timestamp": 1687235603, "status": 6}}
```

## Structure

The project is based in classes. For this we used the next struct
```
project_root/ 
├── main.py 
├── resources/ 
│ ├── __init__.py 
│ ├── measument.py 
│ ├── device_info.py 
│ ├── configuration.py 
│ ├── time.py 
├── Model/ 
│ ├── __init__.py 
│ ├── data.py 
│── utils/ 
│  ├── __init__.py 
│  ├── utilis.py 
├── client/
│  ├── ThingworxClient.py 
├── server/
│  ├── server.py 
├── protobuf/ 
│ ├── __init__.py 
│ ├── proto_cloud_token_config_pb2.py 
│ ├── proto_config_pb2.py 
│ ├── proto_device_info_pb2.py 
│ ├── proto_measument_types_pb2.py 
│ ├── proto_measuments_pb2.py 
│ ├── proto_rule_pb2.py
├── logs/
├── logsConfig.py
```
- __Server.py__: responsible for start the server, and create all the endpooints
- __Data.py__: responsible for create the final struct for send to thingworx
- __utilis.py__: responsible for having functions that used multiples times on the project 
- __measument.py__: responsible for receive frames type measument in format protobuf and deserialise the frame
- __device_info.py__: responsible for receive frames type device_info in format protobuf and deserialise the frame
- __configuration.py__: responsible for receive frames type configuration in format protobuf and deserialise the frame
- __ThingworxClient.py__: responsible for send the frames in format json to thingworx
- __protobuf/__: responsible for desserialize and serialize data, for each type of frame
- __logs/__: save the logs from the server into files
- __main.py__: responsible for keeping the server alive
- __logsConfig.py__: responsible for choose the logs types will appear on logs files

## How to run
To run you must to use python 3.9 and have all the libraries intalled.

### Installation

 

1. Clone the repository:

 

   ```bash
   git clone https://github.gsissc.myatos.net/ES-MAD-VODAFONE-IDL/EfentoCoapBroker.git
   cd EfentoCoapBroker
2. Install the required dependencies:
	```bash
	pip install -r requirements.txt  
3. Run the project:
	```bash
	python3 main.py


# Contribute
Efento coap server
https://getefento.com/library/efento-nbiot-sensors-coap-loader-integration/

Efento Coap Loader
https://getefento.com/library/efento-nb-iot-sensors-integration-with-a-python-coap-server/

### Autors
- Guilherme Correia
- Denis Botnaru


