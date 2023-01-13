import http.client
import json
import datetime
from util import SortUtil

#Original code:
'''print('Start')
start = datetime.datetime.now()
conn = http.client.HTTPSConnection('api.spaceflightnewsapi.net')
headers = {'Content-type': 'application/json'}
conn.request("GET", "/v3/articles?_limit=30", headers=headers)
response = conn.getresponse()
js = json.loads(response.read().decode())
sort_util = SortUtil()
sorted_list = sort_util.sorted_results(js)
for item in sorted_list:
    print(item)
conn.close()
diff = datetime.datetime.now() - start
print('End {} seconds '.format(diff.total_seconds()))'''

#Edited Code:
class GetandSortData:
    global start 
    start = datetime.datetime.now()
    
    def __init__(self, link, request):
      self.link = link
      self.request = request

    #Establish connection and get data
    def establishConnection(self, link, request):
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
    def sortData(self, data):
        sort_util = SortUtil()
        sorted_list = sort_util.sorted_results(data)
        for item in sorted_list:
            print(item)

    #Calculate time taken
    def closeConnection(self):
        #conn.close() 
        diff = datetime.datetime.now() - start
        print('End {} seconds '.format(diff.total_seconds()))

getData = GetandSortData('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')        
dataList = getData.establishConnection('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
getData.sortData(dataList)
getData.closeConnection()