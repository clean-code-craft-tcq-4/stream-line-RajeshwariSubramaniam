import io
import json
import sys
from unittest import TestCase

from bms_data_streamer.data_streamer import DataStreamer


class TestDataSender(TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
        self.streamer = DataStreamer({'foo': ['bar', 'bla']})

    def test_stream_data_in_json(self):
        self.streamer.stream_data_in_json()
        console_output = self.capturedOutput.getvalue()
        self.assertEqual('{"foo": ["bar", "bla"]}\n', console_output)
        self.assertTrue(isinstance(json.loads(console_output), dict))

    def test_stream_data_in_string_with_value_containing_list(self):
        self.streamer.stream_data_in_string()
        console_output = self.capturedOutput.getvalue()
        self.assertEqual('foo:bar\nfoo:bla\n', console_output)

    def test_stream_data_in_string_with_value_containing_string(self):
        self.streamer = DataStreamer({'foo': 'bar'})
        self.streamer.stream_data_in_string()
        console_output = self.capturedOutput.getvalue()
        self.assertEqual('foo:bar\n', console_output)

    def test_check_value_type(self):
        self.assertEqual(
            self.streamer.check_value_type(['bar', 'bla']),
            ['bar', 'bla']
        )
        self.assertEqual(
            self.streamer.check_value_type('bar'),
            ['bar']
        )
