import sqlite3

db = "db.db"
table = "measurements"


def create_db() -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {table}
                   (timestamp real, PM2_5 real, PM10 real, pressure real, temperature real)''')
    con.commit()
    con.close()


def save_measurement(measurement: dict) -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()

    statement = f'''insert into {table} (timestamp, PM2_5, PM10, pressure, temperature)
        values ({measurement["timestamp"]}, {measurement["PM2_5"]}, {measurement["PM10"]}, {measurement["pressure"]}, {measurement["temperature"]})'''

    cur.execute(statement)
    con.commit()
    con.close()


def read_measurements(from_: int , to: int) -> list:
    keys = ["timestamp", "PM2_5", "PM10", "pressure", "temperature"]
    measurements = []

    con = sqlite3.connect(db)
    cur = con.cursor()
    statement = f'''SELECT * FROM {table} WHERE timestamp >= {from_} AND timestamp  <= {to}'''
    records = cur.execute(statement)
    for record in records:
        measurements.append(convert_to_dict(keys, record))

    con.close()

    return measurements


def convert_to_dict(keys: list, values: list) -> dict:
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict