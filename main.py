import http.client
import json
import datetime
from util import SortUtil

if __name__ == "__main__":
  print('Start')
  start = datetime.datetime.now()
  #print(start)
  #conn = http.client.HTTPSConnection('test.spaceflightnewsapi.net')
  conn = http.client.HTTPSConnection('api.spaceflightnewsapi.net')
  headers = {'Content-type': 'application/json'}
  #conn.request("GET", "/api/v2/articles?_limit=30", headers=headers)
  #conn.request("GET", "api.spaceflightnewsapi.net/v3/articles", headers=headers)
  conn.request("GET", "/v3/articles")
  r1 = conn.getresponse()
  print(r1.status, r1.reason)
  #response = conn.getresponse()
  #print(response.read().decode())
  
  try:
     js = json.loads(r1.read().decode())
     sorted_results(js)
     conn.close()
     diff = datetime.datetime.now() - start
     print('End {} seconds '.format(diff.total_seconds()))
  except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')
    

#comment out original code:
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

