import http.client
import json

# Purpose of class: to make Http request to specified URI using GET request to retrieve data
class HttpRequestResponse:
    def __init__(self, link, request):
      self.link = link
      self.request = request

    #Establish connection and get data
    def establish_connection(self, link, request, start):
        print('----------Start----------')
        print("Start Time: " + str(start))
        conn = http.client.HTTPSConnection(self.link)
        headers = {'Content-type': 'application/json'}
        conn.request("GET", self.request, headers=headers)
        response = conn.getresponse()
        js = json.loads(response.read().decode())
        conn.close() 
        return js

    #print time taken
    def print_time_taken(self, diff):
        print('End {} seconds '.format(diff.total_seconds()))