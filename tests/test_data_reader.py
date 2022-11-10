import os
from unittest import TestCase
from unittest.mock import patch

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

    def test_get_readings_from_file(self):
        file_path = os.path.join(self.readings_path, 'test_data.txt')
        with open(file_path) as fr:
            next(fr)
            expected = fr.read().split('\n')
        actual = self.reader.get_readings_from_file(file_path)
        self.assertEqual(expected[0], actual[0])

    def test_readings_from_files(self):
        expected_readings = [12, 23, 26]
        with patch('bms_data_streamer.data_reader.'
                   'FileDataReader.get_readings_from_file',
                   return_value=expected_readings):
            actual_readings = self.reader.readings_from_files('.txt')
        self.assertEqual(expected_readings[0], actual_readings['test_data'][0])
