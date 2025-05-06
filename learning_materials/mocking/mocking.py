import unittest
from unittest.mock import patch, MagicMock
import requests

# Example function to be tested
def fetch_data_from_api(api_url):
    # Simulate an API call
    response = requests.get(api_url)
    return response.json()

class TestMockingExample(unittest.TestCase):
    @patch('requests.get')  # Mock the 'requests.get' method
    def test_fetch_data_from_api(self, mock_get):
        # Create a mock response object
        mock_response = MagicMock()
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        # Call the function
        result = fetch_data_from_api('http://fakeapi.com/data')

        # Assertions
        mock_get.assert_called_once_with('http://fakeapi.com/data')
        self.assertEqual(result, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()