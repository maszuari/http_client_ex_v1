import time
import unittest
import datetime
import io
import sys
from sort.index.reader import HttpRequestResponse
from sort.index.util import SortUtil

class TestFunctions(unittest.TestCase):

    def test_establish_connection(self):
        start = datetime.datetime.now()
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        data = self.assertIsNotNone(connection.establish_connection(start))

    def test_print_time_taken(self):
        start = datetime.datetime.now()
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        #add delay so that can calculate time difference
        time.sleep(2)
        diff = datetime.datetime.now() - start
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        connection.print_time_taken(diff)               # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        print ('Captured', capturedOutput.getvalue())   # Now works as before.

    def test_sorted_results(self):
        start = datetime.datetime.now()
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        data_list = connection.establish_connection(start)
        sort_util = SortUtil()
        self.assertIsNotNone(sort_util.sorted_results(data_list, True))

    def test_print_sorted_results(self):
        start = datetime.datetime.now()
        connection = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
        data_list = connection.establish_connection(start)
        sort_util = SortUtil()
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        sort_util.print_sorted_data(data_list)  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        print('Captured', capturedOutput.getvalue())  # Now works as before.

if __name__ == '__main__':
    unittest.main()