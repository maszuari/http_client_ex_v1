class SortUtil:

	def sorted_results(self, out):
		'''
		This function will sort the data.
		param out: Python object.
		'''
		list = []
		for obj in out:
			list.append(obj['title'])
		
		sorted_list = sorted(list, key=str.lower)
		return sorted_list
