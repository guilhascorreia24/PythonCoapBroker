import asyncio
import base64
import json
import requests
import aiocoap.resource as resource
import aiocoap
from client.ThingworxClient import APPKEY, URLSendInfoDevice
from protobuf import proto_device_info_pb2
from google.protobuf.json_format import MessageToDict
from logsConfig import setup_logging


logger = setup_logging()
class DeviceInfo(resource.Resource):
    def __init__(self):
        super().__init__()

        """Get the device information frames from devices and deserialise this  so he can send to thingworx

        Returns:
            _type_: Message
        """   
    @asyncio.coroutine
    def render_post(self, request):
        logger.debug("hello devic einfo")
        logger.info(" request: " + str(request) +
              " payload: " + str(request.payload))
        info=MessageToDict(proto_device_info_pb2.ProtoDeviceInfo().FromString(request.payload))
        if(info!={}):
            logger.info(info)
            info["serialNum"]=base64.b64decode((info['serialNum'])).hex().upper()
            info=json.dumps(info)
            logger.debug(info)
            headers={'Appkey':APPKEY,'Content-Type':'application/json',"Accept":"application/json"}
            post=requests.post(URLSendInfoDevice, json={"deviceJson":info}, headers=headers)
            logger.debug(post.content)
            # returning "ACK" to the sensor
        response = aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                token=request.token, payload="")
        logger.info(" response: " + str(response))
        return response

    @asyncio.coroutine
    def render_get(self, request):
        return aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.GET,
                               token=request.token, payload="")
