from sort.index.reader import HttpRequestResponse
import datetime
from sort.index.util import SortUtil

#get current time
start = datetime.datetime.now()

#create instance of a class
request_response = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')  

#retrieve data      
data_list = request_response.establish_connection(start) 

#create instance of a class
sort_util = SortUtil()

if data_list != None:
  #sort data
  sorted_list = sort_util.sorted_results(data_list, True)
  #print sorted data
  sort_util.print_sorted_data(sorted_list)

#calculate time taken to retrieve data
diff = datetime.datetime.now() - start

#print time taken to retrieve data
request_response.print_time_taken(diff)
