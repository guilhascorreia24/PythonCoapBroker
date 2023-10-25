
import requests
from logsConfig import setup_logging
logger = setup_logging()

URLSendMeasument = "<url_to_send_measurment>" #changing to message receive efento
URLCheckConfig = "<url_check-Config>"
URLSendInfoDevice = "<url_get_info_device>"
APPKEY = "<api_key>"


"""
    Send the message with the measurment values to the thingworx 
    Return: confirmation
    Type:Response
    """
def RESTPost(message, url=URLSendMeasument, headers={'Appkey': APPKEY, 'Content-Type': 'application/json',"Accept":"application/json"}):
    print(message)
    post = requests.post(url, json={"payload": message}, headers=headers)
    logger.info('Thingworx post: URL -  ' + url +
                 " PAYLOAD -  " + str(message))

    print("Status code" + str(post.content))
    return post