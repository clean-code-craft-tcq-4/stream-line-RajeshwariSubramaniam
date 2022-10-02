import os

from bms_data_streamer.data_reader import FileDataReader
from bms_data_streamer.data_streamer import DataStreamer


def get_sensors_readings_from_files():
    script_path = os.path.abspath(__file__)
    readings_path = os.path.join(
        os.path.dirname(script_path),
        'sensor_readings'
    )
    reader = FileDataReader(
        path=readings_path,
    )
    readings = reader.get_readings_from_files(extension='.txt')
    return readings


def send_sensors_data():
    sensors_readings = get_sensors_readings_from_files()
    sender = DataStreamer(sensors_readings)
    sender.stream_data_in_string()
    # In case a json output is expected uncomment
    # below line and comment json output
    # sender.stream_data_in_json()


if __name__ == '__main__':
    send_sensors_data()
