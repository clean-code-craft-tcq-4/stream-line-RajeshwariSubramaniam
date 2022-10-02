import os
from unittest import TestCase

from bms_data_streamer.data_reader import FileDataReader

script_path = os.path.abspath(__file__)


class TestDataReader(TestCase):
    def setUp(self):
        self.readings_path = os.path.join(
            os.path.dirname(script_path),
            'resources',
        )
        self.reader = FileDataReader(self.readings_path)

    def test_readings_path(self):
        self.assertTrue(isinstance(self.reader.readings_path, str))

        self.reader._readings_path = 'barfoo'
        with self.assertRaises(AssertionError):
            self.reader.readings_path

    def test_get_files_list(self):
        extensions = ['.txt', 'txt', 'test_data.txt']
        for extension in extensions:
            files = self.reader.get_files_list(extension)
            self.assertTrue(os.path.exists(files[0]))

        with self.assertRaises(FileNotFoundError):
            self.reader.get_files_list('foobar')

    def test_get_readings_from_files(self):
        with open(os.path.join(self.readings_path, 'test_data.txt')) as fr:
            next(fr)
            expected = fr.read().split('\n')
        actual = self.reader.get_readings_from_files('.txt')
        self.assertEqual(expected[0], actual['test_data'][0])
