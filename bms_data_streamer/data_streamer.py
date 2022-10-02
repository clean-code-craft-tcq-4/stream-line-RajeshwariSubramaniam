import json


class DataStreamer:
    def __init__(self, data: dict):
        self.data = data

    def stream_data_in_json(self):
        print(json.dumps(self.data))

    def stream_data_in_string(self):
        for sensor, readings in self.data.items():
            for reading in readings:
                print(sensor + ':' + str(reading))
