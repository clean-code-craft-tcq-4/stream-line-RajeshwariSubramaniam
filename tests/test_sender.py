from unittest import TestCase
from unittest.mock import patch

from bms_data_streamer.sender import (
    get_sensors_readings_from_files,
    send_sensors_data
)


class TestSender(TestCase):

    def setUp(self):
        self.readings = {'foobar': [1, 2, 3]}

    def test_get_sensors_readings_from_files(self):
        with patch('bms_data_streamer.data_reader.'
                   'FileDataReader.readings_from_files',
                   return_value=self.readings):
            actual = get_sensors_readings_from_files()
        self.assertEqual(self.readings, actual)

    def test_send_sensors_data(self):
        with patch('bms_data_streamer.sender.'
                   'get_sensors_readings_from_files',
                   return_value=self.readings):
            with patch('builtins.print') as mock_print:
                send_sensors_data()
        mock_print.assert_called()
