import http.client
import json

def sorted_results(out):
    list = []
    for obj in out:
        list.append(obj['title'])
    
    sorted_list = sorted(list, key=str.lower)
    for obj in sorted_list:
        print(obj)


conn = http.client.HTTPSConnection('test.spaceflightnewsapi.net')
headers = {'Content-type': 'application/json'}
conn.request("GET", "/api/v2/articles?_limit=10", headers=headers)
response = conn.getresponse()
js = json.loads(response.read().decode())
sorted_results(js)
conn.close()

