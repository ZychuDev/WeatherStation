import time

from MeasurementCollecting import ConnectorsMock as Connectors
import Database

time_between_queries_in_s = 1

if __name__ == '__main__':
    Database.create_db()

    wait_start_time = time.time()
    current_wait_time = 0

    while True:
        while current_wait_time < time_between_queries_in_s:
            current_wait_time = time.time() - wait_start_time

        values = Connectors.get_values()
        Database.save_measurement(values)

        current_wait_time = 0
        wait_start_time = time.time()
