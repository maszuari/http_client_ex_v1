import unittest
import datetime
from sort.index.reader import HttpRequestResponse
from sort.index.util import SortUtil
import responses
import requests
import httpx
import respx
from httpx import Response
from mock import patch

class TestFunctions(unittest.TestCase):
    #@responses.activate #second method
    @respx.mock
    @patch('sort.index.reader.HttpRequestResponse.establish_connection')
    def test_establish_connection(self, get_connection_mock):
        start = datetime.datetime.now()
        #Test connection. First method
        my_route = respx.get("https://api.spaceflightnewsapi.net/v3/articles?_limit=30").mock(return_value=Response(204))
        response = httpx.get("https://api.spaceflightnewsapi.net/v3/articles?_limit=30")
        assert my_route.called
        assert response.status_code == 204

        #Test return value
        get_connection_mock.return_value = 'mocked_stuff'
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        self.assertEqual(connection.establish_connection(start), 'mocked_stuff')
        self.assertEqual(get_connection_mock.call_count, 1)
        get_connection_mock.assert_called_once()

        self.assertIsNotNone(connection.establish_connection(start))

        #Test connection. Second method:
        '''responses.add(responses.GET, 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30',
                      json={'error': 'not found'}, status=404)

        resp = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=30')

        assert resp.json() == {"error": "not found"}
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://api.spaceflightnewsapi.net/v3/articles?_limit=30'
        assert responses.calls[0].response.text == '{"error": "not found"}'''''

        #original code:
        '''connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        data = self.assertIsNotNone(connection.establish_connection(start))'''

    @patch('sort.index.util.SortUtil.sorted_results')
    def test_sorted_results(self, get_sorted_results_mock):
        get_sorted_results_mock.return_value = ['Apple', 'Bell', 'Cat']
        self.assertIsNotNone(get_sorted_results_mock)

        data_list = ['Bell', 'Apple', 'Cat']
        sort_util = SortUtil()
        self.assertEqual(sort_util.sorted_results(data_list, False), ['Apple', 'Bell', 'Cat'])

        #original code:
        '''start = datetime.datetime.now()
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        data_list = connection.establish_connection(start)
        sort_util = SortUtil()
        self.assertIsNotNone(sort_util.sorted_results(data_list, True))'''


    #unittest.main()