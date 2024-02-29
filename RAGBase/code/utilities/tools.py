from langchain.tools import BaseTool
from pydantic import Field, BaseModel
from enum import Enum
from typing import Optional, Type
from collections.abc import Callable

class ManshonAreaEnum(str, Enum):
    tokyo = "tokyo"
    saitama = "saitama"
    kanagawa = "kanagawa"
    chiba = "chiba"
    other = "other"

class MansionPriceToolCheckInput(BaseModel):
    rooms: int = Field(..., title="Number of rooms", description="The number of rooms in the mansion.")
    area: str = Field(..., title="Area", description="The area of the mansion in square meters.")


class MansionPriceTool (BaseTool):
    name = "MansionPriceTool"
    description = "This tool calculates the price of a mansion based on the number of rooms and the area of the mansion."

       
    def _run(self, rooms:int, area:ManshonAreaEnum):
        price = rooms * 100000 + self.ManshonAreaToPrice(area)
        return price
    
    def ManshonAreaToPrice(self, area:ManshonAreaEnum):
        if area == "tokyo":
            return 100000
        elif area == "saitama":
            return 80000
        elif area == "kanagawa":
            return 90000
        elif area == "chiba":
            return 70000
        elif area == "other":
            return 60000
        else:
            return 0
    
    async def _arun(self, rooms, area):
        return self._run(rooms, area)
    
    args_schema : Optional[Type[BaseModel]] = MansionPriceToolCheckInput



class IoTDeviceEnum(str, Enum):
    light = "light"
    air_conditioner = "air_conditioner"
    heater = "heater"
    fan = "fan"


class IoTDeviceCommandEnum(str, Enum):
    on = "on"
    off = "off"

class IoTDeviceControlToolCheckInput(BaseModel):
    device_id: IoTDeviceEnum = Field(..., title="Device ID", description="The ID of the IoT device.")
    command: IoTDeviceCommandEnum = Field(..., title="Command", description="The command to send to the IoT device.")


class IotDeviceControlTool (BaseTool):
    name = "IotDeviceControlTool"
    description = "This tool controls an IoT device."



    def _run(self, device_id, command):
        if command == "on":
            status = "Device " + device_id + " is turned on."
        elif command == "off":
            status = "Device " + device_id + " is turned off."
        else:
            status = "Invalid command."

            print("iot device command send." + status)
        return status
    
    async def _arun(self, device_id, command):
        return self._run(device_id, command)
        
    args_schema : Optional[Type[BaseModel]] = IoTDeviceControlToolCheckInput


class LifeKnowledgeSearchConfig(BaseModel):
    chat_history : list
    get_semantic_answer_lang_chain_func : Callable


class LifeKnowledgeSearchTool(BaseTool):
    name = "LifeKnowledgeSearchTool"
    description = "This tool searches for life knowledge."
    input_variables = ["question"]
    config: LifeKnowledgeSearchConfig


    def _run(self, question):
        answer = self.config.get_semantic_answer_lang_chain_func(question, self.config.chat_history)
        return answer


    async def _arun(self, question):
        return self._run(question)
