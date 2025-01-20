from pydantic import BaseModel

class BotData(BaseModel):
    direction: str
    start: bool
    stop: bool
    speed: int

class ArmData(BaseModel):
    baseRight: str
    baseLeft: str
    shoulderDown: str
    shoulderUp: str
    elbowDown: str
    elbowUp: str
    wristDown: str
    wristUp: str
    gripDown: str
    gripUp: str
    motor: bool
