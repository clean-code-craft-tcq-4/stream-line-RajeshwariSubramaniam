import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))

default_path = os.path.join(os.path.dirname(script_dir),
                            'default_readings.txt')


class GenerateReadings:
    def __init__(self,
                 range_min,
                 range_max,
                 file_path=default_path):
        self.range_min = range_min
        self.range_max = range_max
        self._readings_path = file_path

    @property
    def readings_path(self):
        assert os.path.isabs(self._readings_path), \
            'Specified path is not absolute'
        return self._readings_path

    def generate_random_readings(self):
        # range_max is multiplied by 10 inorder to
        # generate decimal values
        random_list = random.sample(range(
            self.range_min,
            self.range_max * 10),
            50
        )
        return [num / 10 for num in random_list]

    def write_readings_to_file(self, readings):
        os.makedirs(os.path.dirname(self.readings_path),
                    exist_ok=True)
        with open(self.readings_path, 'w') as fw:
            fw.write("# This file is auto-generated \n")
            for reading in readings:
                fw.write(str(reading) + '\n')

    def generate_and_write_readings_to_file(self):
        random_readings = self.generate_random_readings()
        self.write_readings_to_file(random_readings)
