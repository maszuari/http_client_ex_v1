from reader import Reader

getData = Reader('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')        
dataList = getData.establish_connection('api.spaceflightnewsapi.net', '/v3/articles?_limit=30')
getData.sort_data(dataList)
getData.close_connection()
