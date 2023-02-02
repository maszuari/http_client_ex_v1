import http.client
import json

# Purpose of class: to make Http request to specified URI using GET request to retrieve data
class HttpRequestResponse:
    def __init__(self, link, request):
      self.link = link
      self.request = request

    #Establish connection and get data #link, request, 
    def establish_connection(self, start):
        print('----------Start----------')
        print("Start Time: " + str(start))

        connected = False
        data_available = False
        try:
         conn = http.client.HTTPSConnection(self.link)
         headers = {'Content-type': 'application/json'}
         conn.request("GET", self.request, headers=headers)
         connected = True
         
        except conn.timeout:
          print("Timeout Error")
        except Exception as err:
          print(f"Unexpected {err=}, {type(err)=}") 

        if connected:
          response = conn.getresponse()
          try:
           js = json.loads(response.read().decode())
           data_available = True
           conn.close() 
          except ValueError:  # includes simplejson.decoder.JSONDecodeError
               print('Decoding JSON has failed') 
        if data_available:  
         return js
        else:
          print("Unable to retrieve data")
          return None #print message
    #print time taken
    def print_time_taken(self, diff):
        print('End {} seconds '.format(diff.total_seconds()))