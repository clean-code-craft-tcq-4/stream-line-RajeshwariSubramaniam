import glob
import os


class FileDataReader:
    def __init__(self, path):
        self._readings_path = path
        self.readings = {}

    @property
    def readings_path(self):
        assert os.path.isabs(self._readings_path), \
            'Specified path is not absolute'
        return self._readings_path

    def get_files_list(self, extension):
        files = glob.glob(self.readings_path + '/*' + extension)
        if not files:
            raise FileNotFoundError
        return files

    def readings_from_files(self, extension: str):
        for file in self.get_files_list(extension):
            file_name = os.path.basename(file)
            bms_parameter = file_name.split('.')[0]
            self.readings[bms_parameter] = self.get_readings_from_file(file)
        return self.readings

    @staticmethod
    def get_readings_from_file(file):
        readings = []
        with open(file, 'r') as f_read:
            for line in f_read:
                if line[:1] == '#':
                    continue
                reading = line.split('\n')[0]
                readings.append(reading)
        return readings
