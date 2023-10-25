
from array import array
import json
from typing import Any
import utils.utils as utils
from logsConfig import setup_logging

logger=setup_logging()

class Data:
    class Params:
    
        """create a instance Params
            """
        def __init__(self, value, type, channel) -> None:
            # print(str(value)+","+str(type)+","+str(channel))
            self.value = value
            self.type = type.lower()
            self.channel = channel
        
        """Creates a string with the instance information
            Returns: str
        """    
        def __str__(self) -> str:
            return str(self.channel)+","+str(self.value)+","+str(self.type)+";"

    
    class Encoder(json.JSONEncoder):
        """create a json for the instance Data
            """
        def default(self, obj):
            if isinstance(obj, Data):
                arr=json.dumps([p.__dict__ for p in obj.params])
                return {"measured_at": obj.measured_at,"serial":obj.serial,"next_measurement_at":obj.next_measurement_at,"signal":obj.signal,"measurement_interval":obj.measurement_interval,"batteryStatus":obj.batteryStatus,"params":json.loads(arr)}
            return json.JSONEncoder.default(self, obj)
    
    """create a instance Data
            """
    def __init__(self,time_measured,measured_at,serial,next_measurement_at,battery=None,params=None,measurement_interval=None,signal=None) -> None:
        #params=[]
        #print(str(time_measured)+","+str(measured_at)+","+str(serial)+","+str(next_measurement)+","+str(battery)+","+str(params))
        try:
            self.measured_at=measured_at.strftime('%Y-%m-%d %H:%M:%S UTC')
            self.serial=serial.upper()
            self.next_measurement_at=next_measurement_at.strftime('%Y-%m-%d %H:%M:%S UTC')
            #self.time_measured=time_measured.isoformat()
            if signal is None: self.signal=0
            else: self.signal=signal
            self.measurement_interval=measurement_interval
            if(battery==True):
                self.batteryStatus="ok"
            else:
                self.batteryStatus="low"
            if params is None:
                params=[]
            self.params=params
        except Exception as e:
            logger.error("error "+e)
    
        """Check if 2 instance type Data are the same 
            Returns: bool
        """    
    def __eq__(self, other)->bool:
        if not isinstance(other,Data):
            return NotImplemented
        return self.serial==other.serial and self.measured_at==other.measured_at
    
    """Creates a string with the instance information
            Returns: str
        """    
    def __str__(self) -> str:
        res=str(self.measured_at)+","+str(self.batteryStatus)+","+str(self.serial)+","+str(self.next_measurement_at)+","+str(self.measurement_interval)+",["
        for x in self.params:
            res+=str(x)
        return res+"]"
    
    

    


