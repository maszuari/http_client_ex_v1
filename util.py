class SortUtil:

  def sorted_results(self, out):
	 #This function will sort the data. param out: Python object.
    list = []
    for obj in out:
     list.append(obj['title'])
    
    sorted_list = sorted(list, key=str.lower)
    return sorted_list
  
  #Print sorted data
  def print_sorted_data(self, data):
        sorted_list = self.sorted_results(data)
        for item in sorted_list:
            print(item)			




