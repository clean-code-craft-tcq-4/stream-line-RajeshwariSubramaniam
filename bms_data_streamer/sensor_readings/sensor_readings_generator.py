import os

from bms_data_streamer.resources.readings_generator \
    import GenerateReadings

script_path = os.path.abspath(__file__)

sensors = {
    'Temperature': {'minimum': -70, 'maximum': 200},
    'State_Of_Charge': {'minimum': 0, 'maximum': 50},
    }


def generate_sensor_readings():
    for sensor, value_range in sensors.items():
        readings_path = os.path.join(
            os.path.dirname(script_path),
            sensor.lower() + '.txt'
        )
        generator = GenerateReadings(
            readings_path,
            value_range['minimum'],
            value_range['maximum']
        )
        generator.write_readings_to_file()


if __name__ == '__main__':
    generate_sensor_readings()
