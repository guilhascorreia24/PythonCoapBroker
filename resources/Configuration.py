
import asyncio
import base64

import json

import requests
import aiocoap.resource as resource
import aiocoap
from client.ThingworxClient import APPKEY, URLCheckConfig
from protobuf import proto_config_pb2
from google.protobuf.json_format import MessageToDict
from logsConfig import setup_logging


logger = setup_logging()

class Configuration(resource.Resource):
    def __init__(self):
        super().__init__()

        """Get the configuration frames from devices and deserialise this  so he can send to thingworx

        Returns:
            _type_: Message
        """    
    @asyncio.coroutine
    def render_post(self, request):
        data = MessageToDict(proto_config_pb2.ProtoConfig().FromString(request.payload))
        data["serialNumber"]=base64.b64decode((data['serialNumber'])).hex().upper()
        dataToCheck=json.dumps(data)
        logger.info("data configuration"+str(dataToCheck))
        logger.info("type:"+str(type(dataToCheck)))
        headers={'Appkey':APPKEY,'Content-Type':'application/json',"Accept":"application/json"}
        post=requests.post(URLCheckConfig, json={"device": str(data["serialNumber"]),"configuration":data}, headers=headers)
        logger.debug("status:"+str(post.status_code))
        logger.debug("content:"+str(post.content))
        response = aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                                   token=request.token, payload="")
        logger.info(" response: " + str(response))
        return response

    # Time - Class used to handle Time messages sent by the sensor

