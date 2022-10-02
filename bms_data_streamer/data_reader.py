import glob
import os


class FileDataReader:
    def __init__(self, path):
        self._readings_path = path

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

    def get_readings_from_files(self, extension: str):
        readings = {}
        for file in self.get_files_list(extension):
            bms_parameter = os.path.basename(file)
            readings[bms_parameter] = []
            for line in self.read_file(file):
                if line[:1] == '#':
                    continue
                reading = line.split('\n')[0]
                readings[bms_parameter].append(reading)
        return readings

    @staticmethod
    def read_file(file):
        with open(file, 'r') as f_read:
            for line in f_read:
                yield line
