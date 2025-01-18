import json
import serial
import asyncio
import threading
from config import SERIAL_PORT, BAUD_RATE

# Shared dictionary for sensor data
sensor_data = {
    "temperature": None,
    "humidity": None,
    "windSpeed": None,
    "dustParticles": None,
    "soilTemperature": None,
    "soilPH": None,
    "soilMoisture": None
}

async def serial_reader(broadcast_callback):
    """ Continuously read data from Arduino and update the sensor dictionary """
    global sensor_data
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        while True:
            try:
                line = ser.readline().decode("utf-8").strip()
                if line:
                    data = json.loads(line)
                    sensor_data.update(data)
                    await broadcast_callback(sensor_data)  # Notify WebSocket clients
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass
    except serial.SerialException as e:
        print(f"Serial Error: {e}")

def start_serial_thread(broadcast_callback):
    """ Start the serial reader in a separate thread """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(serial_reader(broadcast_callback))

def run_serial_reader(broadcast_callback):
    """ Launch serial reader thread """
    serial_thread = threading.Thread(target=start_serial_thread, args=(broadcast_callback,), daemon=True)
    serial_thread.start()
