from reader import HttpRequestResponse
import datetime
from util import SortUtil

#get current time
start = datetime.datetime.now()

#create instance of a class
getData = HttpRequestResponse('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')  

#retrieve data      
dataList = getData.establish_connection('api.spaceflightnewsapi.net', '/v3/articles?_limit=30', start)

#create instance of a class
sort_util = SortUtil()

#print sorted data
sort_util.print_sorted_data(dataList)

#calculate time taken to retrieve data
diff = datetime.datetime.now() - start

#print time taken to retrieve data
getData.print_time_taken(diff)
