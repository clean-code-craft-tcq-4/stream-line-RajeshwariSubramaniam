import json


class DataStreamer:
    def __init__(self, data: dict):
        self.data = data

    def stream_data_in_json(self):
        print(json.dumps(self.data))

    def stream_data_in_string(self):
        for key, value in self.data.items():
            values = self.check_value_type(value)
            for val in values:
                print(key + ':' + str(val))

    @staticmethod
    def check_value_type(value):
        if isinstance(value, list):
            return value
        return [value]
