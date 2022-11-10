from unittest import TestCase
from unittest.mock import patch

from bms_data_streamer.resources.sensor_readings_generator \
    import generate_sensor_readings_files


class TestSensorReadingsGenerator(TestCase):

    def test_generate_sensor_readings_files(self):
        with patch('bms_data_streamer.resources.lib.'
                   'readings_generator.GenerateReadings.'
                   'generate_and_write_readings_to_file') as mock_generate:
            generate_sensor_readings_files()
        mock_generate.assert_called()
