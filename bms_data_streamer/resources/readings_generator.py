import os
import random

script_path = os.path.abspath(__file__)


class GenerateReadings:
    def __init__(self,
                 readings_path,
                 range_min=0,
                 range_max=1000):
        self.range_min = range_min
        self.range_max = range_max
        self.readings_path = readings_path

    def generate_random_readings(self):
        # range_max is multiplied by 10 inorder to
        # generate decimal values
        random_list = random.sample(range(
            self.range_min,
            self.range_max*10),
            50
        )
        return [num/10 for num in random_list]

    def write_readings_to_file(self):
        random_readings = self.generate_random_readings()
        os.makedirs(os.path.dirname(self.readings_path),
                    exist_ok=True
                    )
        with open(self.readings_path, 'w') as fw:
            fw.write("# This file is auto-generated \n")
            for reading in random_readings:
                fw.write(str(reading) + '\n')
