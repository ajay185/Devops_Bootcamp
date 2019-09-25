import json

from unittest import TestCase
from unittest.mock import patch

import requests


class TestRestAPI(TestCase):

    @patch('requests.post')
    def test_post(self, mock_post):
        info = {"test1": "value1", "test2": "value2"}
        resp = requests.post("www.someurl.com", data=json.dumps(info), headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("www.someurl.com", data=json.dumps(info), headers={'Content-Type': 'application/json'})


##TestRestAPI().test_post()