import asyncio
from google.protobuf.json_format import MessageToDict
from logsConfig import setup_logging
from server.Server import start_server


"""Keeps the server alive
    """
logger = setup_logging()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())