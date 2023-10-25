
import asyncio
import time

import aiocoap.resource as resource
import aiocoap
from google.protobuf.json_format import MessageToDict
from Model import Data
from logsConfig import setup_logging


logger = setup_logging()
class Time(resource.Resource):
    def __init__(self):
        super().__init__()

    @asyncio.coroutine
    def render_post(self, request):
        logger.debug("hello time")
        logger.info(" request: " + str(request) +
              " payload: " + str(request.payload.hex()))
        time_stamp = int(time.time())
        time_stamp_hex = hex(time_stamp)
        # returning timestamp to the sensor
        response = aiocoap.Message(mtype=aiocoap.ACK, code=aiocoap.Code.CREATED,
                                   token=request.token, payload=bytearray.fromhex(time_stamp_hex[2:]))
        logger.info(" response: " + str(response) +
                     " payload: " + str(response.payload.hex()))
        return response

