
import asyncio
import aiocoap.resource as resource
import aiocoap
from google.protobuf.json_format import MessageToDict
from logsConfig import setup_logging
from resources.Configuration import Configuration
from resources.DeviceInfo import DeviceInfo
from resources.Measument import Measument
from resources.Time import Time
logger = setup_logging()

"""
Start the server, creating all the endpoints

    Yields:
        _type_: _description_
"""
@asyncio.coroutine
def start_server():
    root = resource.Site()
    root.add_resource(['m'], Measument())
    root.add_resource(["i"], DeviceInfo())
    # Set up “c” endpoint, which will be receiving configuration messages sent by Efento NB-IoT sensor using POST method
    root.add_resource(["c"], Configuration())
    # Set up “t” endpoint, which will be receiving time sent by Efento NB-IoT sensor using POST method
    root.add_resource(["t"], Time())
    # root.add_resource(['time'], TimeResource())
    server = yield from aiocoap.Context.create_server_context(root, ('::', 4040))
    # server.add_resource(root)
    print("running")
    yield from asyncio.get_event_loop().create_future()