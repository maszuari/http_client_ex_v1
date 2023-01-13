import http.client
import json
import datetime
from util import SortUtil

#Reads the data from the resources
class Reader:
    global start 
    start = datetime.datetime.now()

    def __init__(self, link, request):
      self.link = link
      self.request = request

    #Establish connection and get data
    def establish_connection(self, link, request):
        print('----------Start----------')
        print("Start Time: " + str(start))
        conn = http.client.HTTPSConnection(self.link)
        headers = {'Content-type': 'application/json'}
        conn.request("GET", self.request, headers=headers)
        response = conn.getresponse()
        js = json.loads(response.read().decode())
        conn.close() 
        return js

    #Sort data & print 
    def sort_data(self, data):
        sort_util = SortUtil()
        sorted_list = sort_util.sorted_results(data)
        for item in sorted_list:
            print(item)

    #Calculate time taken
    def close_connection(self):
        #conn.close() 
        diff = datetime.datetime.now() - start
        print('End {} seconds '.format(diff.total_seconds()))