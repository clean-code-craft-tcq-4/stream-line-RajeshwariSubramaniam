import io
import json
import sys
from unittest import TestCase

from bms_data_streamer.data_streamer import DataStreamer


class TestDataSender(TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
        self.sender = DataStreamer({'foo': ['bar']})

    def test_send_data_json(self):
        self.sender.stream_data_in_json()
        console_output = self.capturedOutput.getvalue()
        self.assertEqual('{"foo": ["bar"]}\n', console_output)
        self.assertTrue(isinstance(json.loads(console_output), dict))

    def test_send_data_string(self):
        self.sender.stream_data_in_string()
        console_output = self.capturedOutput.getvalue()
        self.assertEqual('foo:bar\n', console_output)
