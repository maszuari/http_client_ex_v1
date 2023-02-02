class SortUtil:

  def sorted_results(self, out, descending=False):
   """
		This function will sort the data.
		param out: Python object.
		param descending: If True, result will be in descending order.
		return: Return sorted list
		"""
   list = []
   for obj in out:
     list.append(obj['title'])
		
   sorted_list = sorted(list, key=str.lower, reverse=descending)
   return sorted_list
  
  #Print sorted data
  def print_sorted_data(self, data):
        for item in data:
            print(item)			

  #Filter list by specific character
  def filter_title_by_character(self, data_list, letter):
      # using list comprehension + lower()
      # Words starting with specific letter
      res = [idx for idx in data_list if idx[0].lower() == letter.lower()]
      # print result
      print('\n*******************************************************************')
      print("The list of matching first letter : " + str(res))
      return res