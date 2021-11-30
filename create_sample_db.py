import time

import Database
from MeasurementCollecting import ConnectorsMock
number_of_records = 1000
interval_in_seconds = 60

if __name__ == '__main__':
    Database.create_db()

    time_now = time.time()
    time_start = time_now - number_of_records * interval_in_seconds

    time = time_start
    while time < time_now:
        values = ConnectorsMock.get_values_at_time(time)
        Database.save_measurement(values)

        time += interval_in_seconds


