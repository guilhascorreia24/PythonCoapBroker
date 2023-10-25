import re
from Model import Data
from logsConfig import setup_logging
logger = setup_logging()

"""
Get the configuration json and put this values in correct way into the deviceConfig json
"""

def NewConfigurationToDevice(configuration, deviceConfig):
    for key in configuration:
        if key != "serialNumber" and key != "flag":
            att = re.sub(r'([A-Z])', r'_\1', key).lower()
            value = configuration[key]
            try:  # some properties uses wierd classnames
                if type(configuration[key]) == list:
                    if att == "dns_server_ip":
                        deviceConfig.dns_server_ip.extend(value)
                    elif att == "cellular_config_params":
                        deviceConfig.cellular_config_params.extend(value)
                    elif att == "led_config":
                        deviceConfig.led_config.extend(value)
                setattr(deviceConfig, att, value)
            except Exception as e:
                logger.error(e)
    if deviceConfig != None:
        deviceConfig.request_configuration = True
    return deviceConfig


# You can add more utility functions here if needed
