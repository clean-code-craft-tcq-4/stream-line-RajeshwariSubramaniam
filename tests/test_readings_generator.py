from unittest import TestCase
from unittest.mock import patch

from bms_data_streamer.resources.lib.readings_generator import GenerateReadings


class TestGenerateReadings(TestCase):

    def setUp(self):
        self.generator = GenerateReadings(
            range_max=10,
            range_min=20
        )

    def test_generate_random_readings(self):
        readings = self.generator.generate_random_readings()
        self.assertTrue(isinstance(readings, list))

    def test_readings_path(self):
        self.assertTrue(isinstance(self.generator.readings_path, str))
        self.generator._readings_path = 'foobar'
        with self.assertRaises(AssertionError):
            self.generator.readings_path

    def test_write_readings_to_file(self):
        with patch('os.makedirs'):
            with patch('builtins.open') as mock_file_write:
                self.generator.write_readings_to_file([12, 24, 48])
        mock_file_write.assert_called()

    def test_generate_and_write_readings_to_file(self):
        with patch('bms_data_streamer.resources.lib.'
                   'readings_generator.GenerateReadings.'
                   'generate_random_readings') as mock_generate:
            with patch('bms_data_streamer.resources.lib.'
                       'readings_generator.GenerateReadings.'
                       'write_readings_to_file') as mock_write:
                self.generator.generate_and_write_readings_to_file()
        mock_generate.assert_called()
        mock_write.assert_called()
