import unittest
import pytest
import os
from unittest.mock import Mock, patch, mock_open, MagicMock
from download_file.download import download_file

class TestDownloadFile(unittest.TestCase):
    @staticmethod
    def test_download_file_pass():
        env_variables = TestDownloadFile.env_variables_helper()
        with patch.dict(os.environ, env_variables):
            with patch('requests.get') as get_mock:
                with patch('builtins.open', new_callable=mock_open()) as mock_file:
                    mock_response = Mock(status_code=200)
                    mock_response.content = "somecontent"
                    get_mock.return_value = mock_response
                    download_file()
                    mock_file.assert_called_once_with("somefile.tgz", "wb")

    @staticmethod
    def env_variables_helper():
        return {
            'URL' : 'https://www.google.com',
            'OUTPUT_PATH': 'somefile.tgz'
        }
