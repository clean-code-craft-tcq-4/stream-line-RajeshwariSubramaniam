import os

from bms_data_streamer.resources.lib.readings_generator \
    import GenerateReadings

script_path = os.path.abspath(__file__)

# Sets random values for sensor readings between some range
# if specified, else will use default
bms_parameters = {
    'Temperature': {'minimum': -70, 'maximum': 200},
    'State_Of_Charge': None,
}

sensor_readings_dir = os.path.join(
    os.path.dirname(os.path.dirname(script_path)),
    'sensor_readings',
)


def generate_sensor_readings_files():
    for parameter, value_range in bms_parameters.items():

        _range = value_range if value_range \
            else {'minimum': 0, 'maximum': 500}

        file_path = os.path.join(
            sensor_readings_dir,
            parameter.lower() + '.txt'
        )

        generator = GenerateReadings(
            range_min=_range['minimum'],
            range_max=_range['maximum'],
            file_path=file_path
        )
        generator.generate_and_write_readings_to_file()


if __name__ == '__main__':
    generate_sensor_readings_files()
