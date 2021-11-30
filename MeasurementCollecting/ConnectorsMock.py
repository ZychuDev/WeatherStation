import random
import time


def get_values():
    PM2_5 = random.uniform(1, 10)
    PM10 = random.uniform(1, 10)

    temperature = random.uniform(-10, 10)
    pressure = random.uniform(900, 1100)

    timestamp = int(time.time())

    return {"timestamp": timestamp, "PM2_5": PM2_5, "PM10": PM10, "temperature": temperature, "pressure": pressure}


def get_values_at_time(timestamp):
    values = get_values()
    values["timestamp"] = int(timestamp)
    return values
