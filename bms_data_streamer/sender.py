import json

import bms_data_streamer.data_reader as data_reader


class DataSender:
    def __init__(self):
        self._data = {}

    @property
    def data(self):
        return data_reader.get_sensors_readings_from_file()

    def stream_data_in_json(self):
        print(json.dumps(self.data))


if __name__ == '__main__':
    sender = DataSender()
    sender.stream_data_in_json()

