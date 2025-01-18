from pydantic import BaseModel

class BotData(BaseModel):
    direction: str
    start: bool
    stop: bool
    speed: int

class ArmData(BaseModel):
    base: int
    shoulder: int
    knee: int
    wrist: int
    grip: int
