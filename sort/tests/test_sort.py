import unittest
import datetime
from sort.index.reader import HttpRequestResponse
from sort.index.util import SortUtil
import responses
import requests
from mock import patch

class TestFunctions(unittest.TestCase):
    @patch('sort.index.reader.HttpRequestResponse.establish_connection')
    def test_establish_connection(self, get_connection_mock):
        # Test return value
        start = datetime.datetime.now()
        get_connection_mock.return_value = {"title": "Bell", "title": "Apple", "title": "Cat"}
        mock_value = {"title": "Bell", "title": "Apple", "title": "Cat"}
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        self.assertIsNotNone(connection.establish_connection(start))
        self.assertEqual(connection.establish_connection(start), mock_value)

    @responses.activate
    def test_establish_connection_http_404(self):
        # Test connection. 404: The server cannot find the requested resource
        responses.add(responses.GET, 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30',
                      json={'error': 'not found'}, status=404)

        resp = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=30')

        assert resp.json() == {"error": "not found"}
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30'
        assert responses.calls[0].response.text == '{"error": "not found"}'

    @responses.activate
    def test_establish_connection_http_400(self):
        # Test connection. 400: The server cannot or will not process the request due to something that is perceived to be a client error
        responses.add(responses.GET, 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30',
                      json={'error': 'Invalid status code'}, status=400)

        resp = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=30')

        assert resp.json() == {"error": "Invalid status code"}
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30'
        assert responses.calls[0].response.text == '{"error": "Invalid status code"}'

    @responses.activate
    def test_establish_connection_http_500(self):
        # Test connection. 500: The server encountered an unexpected condition that prevented it from fulfilling the request
        responses.add(responses.GET, 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30',
                      json={'error': 'Internal Server Error'}, status=500)

        resp = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=30')

        assert resp.json() == {"error": "Internal Server Error"}
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30'
        assert responses.calls[0].response.text == '{"error": "Internal Server Error"}'

    @responses.activate
    def test_establish_connection_http_200(self):
        # Test connection. 200: Successful request
        responses.add(responses.GET, 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30',
                      json={'status': 'Accepted'}, status=200)

        resp = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=30')

        assert resp.json() == {"status": "Accepted"}
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30'
        assert responses.calls[0].response.text == '{"status": "Accepted"}'

    @patch('sort.index.reader.HttpRequestResponse.establish_connection')
    def test_sorted_results(self, get_sorted_results_mock):
        get_sorted_results_mock.return_value = {"title": "Bell", "title": "Apple", "title": "Cat"}
        sort_util = SortUtil()
        self.assertIsNotNone(sort_util.sorted_results(get_sorted_results_mock, True))

    def test_filter_title_by_character(self):
        data_list = ['Cally', 'Betty', 'Emily', 'Jacob', 'Josephine', 'Chris']
        sort_util = SortUtil()
        #self.assertIsNone(sort_util.filter_title_by_character(data_list, "J"))
        self.assertEqual(sort_util.filter_title_by_character(data_list, "J"), ['Jacob', 'Josephine'])