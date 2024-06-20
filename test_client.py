from unittest import TestCase
from unittest import mock
import client


class TestGetIp(TestCase):

    def test_empty(self):
        with mock.patch('builtins.input', return_value=""):
            self.assertEqual(client.get_host_ip(), '127.0.0.1')

    def test_valid_ip(self):
        with mock.patch('builtins.input', return_value="0.0.0.0"):
            self.assertEqual(client.get_host_ip(), "0.0.0.0")


class TestGetPort(TestCase):

    def test_empty(self):
        with mock.patch('builtins.input', return_value=""):
            self.assertEqual(client.get_port(), 12345)

    def test_valid(self):
        with mock.patch('builtins.input', return_value=""):
            self.assertEqual(client.get_port(), 12345)

    def test_not_integer(self):
        mocked_inputs = ["a", "b1", "5"]
        inputs = (i for i in mocked_inputs)

        def mock_input(prompt):
            return next(inputs)
        
        with mock.patch('builtins.input', side_effect=mock_input) as mock_in:
            result = client.get_port()
            # Test the inputs are actually being put through
            self.assertEqual(mock_in.call_count, 3)
            self.assertEqual(result, 5)
