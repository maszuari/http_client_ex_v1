import http.client
import json
import datetime
from util import SortUtil

print('Start')
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
print('End {} seconds '.format(diff.total_seconds()))
