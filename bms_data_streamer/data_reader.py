import glob
import os

script_path = os.path.abspath(__file__)


def get_sensors_readings_from_file():
    readings = {}
    readings_files = get_sensor_readings_files_list()
    for file in readings_files:
        with open(file) as fr:
            sensor = os.path.basename(fr.name).split('.')[0]
            readings[sensor] = []
            for line in fr:
                if line.startswith('#'):
                    continue
                readings[sensor].append(line)
    return readings


def get_sensor_readings_files_list():
    readings_path = os.path.join(
        os.path.dirname(script_path),
        'sensor_readings'
    )
    files = glob.glob(readings_path + '/*.txt')
    return files
