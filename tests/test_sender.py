import io
import json
import sys
from unittest import TestCase

from bms_data_streamer.sender import DataSender


class TestDataSender(TestCase):
    def test_send_data(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sender = DataSender()
        sender.stream_data_in_json()
        console_output = capturedOutput.getvalue()
        self.assertTrue(isinstance(json.loads(console_output), dict))
