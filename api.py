from fastapi import APIRouter
from fastapi.responses import JSONResponse
from serial_reader import sensor_data

router = APIRouter()

@router.get("/soil-temperature")
async def get_soil_temperature():
    """ REST API endpoint to fetch soil temperature """
    return JSONResponse(content={"soilTemperature": sensor_data.get("soilTemperature")})

@router.get("/soil-ph")
async def get_soil_ph():
    """ REST API endpoint to fetch soil pH """
    return JSONResponse(content={"soilPH": sensor_data.get("soilPH")})

@router.get("/soil-moisture")
async def get_soil_moisture():
    """ REST API endpoint to fetch soil moisture """
    return JSONResponse(content={"soilMoisture": sensor_data.get("soilMoisture")})

