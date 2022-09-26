import io
import json
import sys
from unittest import TestCase


class TestDataSender(TestCase):
    def test_send_data(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        # Add the source and then call the relevant function() here for testing
        console_output = capturedOutput.getvalue()
        self.assertTrue(isinstance(json.loads(console_output), dict))
