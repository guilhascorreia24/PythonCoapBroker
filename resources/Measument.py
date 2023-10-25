import asyncio
import base64
import datetime
import json
import time
import aiocoap.resource as resource
import aiocoap
from client.ThingworxClient import RESTPost
from protobuf import proto_measurements_pb2
from protobuf import proto_config_pb2
from google.protobuf.json_format import MessageToDict
from Model.Data import Data
from logsConfig import setup_logging
import utils.utils as utils
logger = setup_logging()


class Measument(resource.Resource):
    def __init__(self):
        # Initialize any necessary variables or configurations here
        pass

        """
        Get the param, value and channel and translate this into understandable information, translating the value, timestamp, battery and etc, this is for the devices that has non binary values like temperature and humidity sensors
        Save this information in measuement list
        _type_:None 
        """

    def process_generic_measurement(self, param, measurement, measurements, record, channel):
        logger.debug("process_generic_measurement")
        try:

            for index, sampleOffset in enumerate(param['sampleOffsets']):
                if param['type'] == "MEASUREMENT_TYPE_TEMPERATURE" or param['type'] == "MEASUREMENT_TYPE_ATMOSPHERIC_PRESSURE":
                    value = (param['startPoint'] + sampleOffset) / 10
                else:
                    value = param['startPoint'] + sampleOffset
                timeDifference = measurement['measurementPeriodBase'] * index
                battery = measurement.get("batteryStatus")
                record.append((
                    datetime.datetime.fromtimestamp(
                        param['timestamp'] + timeDifference),
                    base64.b64decode(measurement['serialNum']).hex(),
                    battery,
                    param['type'].replace("MEASUREMENT_TYPE_", ""),
                    value
                ))

                self.create_data_item(
                    measurements,
                    param['timestamp'] + timeDifference,
                    param['timestamp'] + timeDifference +
                    measurement['measurementPeriodBase'],
                    base64.b64decode(measurement['serialNum']).hex(),
                    battery,
                    param['type'].replace("MEASUREMENT_TYPE_", ""),
                    channel,
                    value, measurement
                )
        except Exception as e:
            logger.error("process_generic_measurement:", str(e))

        """Get deserialise data and check the type of sensor
            Returns:
            information about the meassument in the correct way 
            _type_: list
        """

    def process_measurement_data(self, data):
        try:
            measurements = []
            record = []
            channel = 0
            for measurement in data:
                for param in measurement['channels']:
                    if param:
                        channel += 1
                        if param['type'] == "MEASUREMENT_TYPE_OK_ALARM":
                            print("ok alamr")
                            self.process_ok_alarm_measurement(
                                param, measurement, measurements, record, channel)
                        else:
                            self.process_generic_measurement(
                                param, measurement, measurements, record, channel)

            return measurements, record
        except Exception as e:
            logger.error(e)

        """Get the param, value and channel and translate this into understandable information, translating the value, timestamp, battery and etc, this is for the devices that has binary values like Water Leak 
            eg: Alarm->open 
            Save this information in measuement list
            Returns:
            _type_:None
        """

    def process_ok_alarm_measurement(self, param, measurement, measurements, record, channel):
        logger.debug("process_ok_alarm_measurement")
        try:
            numberOfMeasurements = 1 + \
                (abs(param['sampleOffsets'][-1]) - 1) / \
                measurement['measurementPeriodBase']
            changeAt = []

            for sampleOffset in param['sampleOffsets']:
                timeDifference = measurement['measurementPeriodBase'] * int(
                    abs(sampleOffset - 1) / measurement['measurementPeriodBase'])
                if sampleOffset > 0:
                    changeAt.extend(
                        [param['timestamp'] + timeDifference, "Alarm"])
                elif sampleOffset < 1:
                    changeAt.extend(
                        [param['timestamp'] + timeDifference, "OK"])

            for measurementNumber in range(int(numberOfMeasurements)):
                timeDifference = measurement['measurementPeriodBase'] * \
                    measurementNumber
                if param['timestamp'] + timeDifference in changeAt:
                    value = changeAt[changeAt.index(
                        param['timestamp'] + timeDifference) + 1]

                battery = measurement.get('batteryStatus')
                record.append((
                    datetime.datetime.fromtimestamp(
                        param['timestamp'] + timeDifference),
                    base64.b64decode(measurement['serialNum']).hex(),
                    battery,
                    param['type'].replace("MEASUREMENT_TYPE_", ""),
                    "open" if value == "Alarm" else "closed"
                ))

                self.create_data_item(
                    measurements,
                    param['timestamp'] + timeDifference,
                    param['timestamp'] + timeDifference +
                    measurement['measurementPeriodBase'],
                    base64.b64decode(measurement['serialNum']).hex(),
                    battery,
                    "open-close",
                    channel,
                    value,
                    measurement
                )
        except Exception as e:
            logger.error("error process_ok_alarm_measurement:", str(e))

        """
        Create the final struct of data deserialised before sending to thingworx

        Returns:
            _type_: None
        """

    def create_data_item(self, measurements, start_time, end_time, serial_num, battery, value_type, channel, value, measurement):
        logger.debug("create_data_item")
        try:
            data_item = Data(
                datetime.datetime.fromtimestamp(start_time),
                datetime.datetime.fromtimestamp(start_time),
                serial_num,
                datetime.datetime.fromtimestamp(end_time),
                battery,
                None,
                measurement['measurementPeriodBase']
            )

            if data_item not in measurements:
                data_item.params.append(
                    Data.Params(value, value_type, channel))
                measurements.append(data_item)
            else:
                data1 = next((x for x in measurements if x == data_item), None)
                if data1:
                    data1.params.append(Data.Params(
                        value, value_type, channel))
        except Exception as e:
            logger.error("Error creating Data item:", str(e))

        """
        Get the measument frames from devices and deserialise this  so he can send to thingworx, and the confirmation to the device with the deviceConfig json

        Returns:
            _type_: Message
        """
    @asyncio.coroutine
    def render_post(self, request):
        try:
            timestamp = time.time()
            logger.info("received payload: " + str(request.payload))
            data = [MessageToDict(
                proto_measurements_pb2.ProtoMeasurements().FromString(request.payload))]
            json_record = {}
            print(data)
            measurements, record = self.process_measurement_data(data)
            response_payload = ""
            response = ""
            device_config = proto_config_pb2.ProtoConfig()

            try:
                json_record["measurements"] = json.loads(json.dumps(
                    measurements, cls=Data.Encoder).replace("\\", ''))
                json_record2 = json.dumps(json_record)
                logger.info("Payload to send: " + str(json_record2))
                post = RESTPost(json_record2)
                post = json.loads(post.content.decode("utf-8"))
                if post["status"] == 200:
                    device_config = utils.NewConfigurationToDevice(
                        post["RemoteConfiguration"], device_config)
                device_config.request_configuration = True
                response_payload = device_config.SerializeToString()
            except Exception as e:
                logger.error("Error in payload processing:", str(e))
            response = aiocoap.Message(
                mtype=aiocoap.ACK, code=aiocoap.Code.CREATED, token=request.token, payload=response_payload)
            logger.info("send Ack: " + str(response.payload))
            return response
        except Exception as e:
            logger.error("Top-level error:" + str(e))
