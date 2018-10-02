"""
page 33

"""

# Python question
# https://www.tutorialspoint.com/python/dictionary_values.htm
# values() should return type list but instead type dict_values; why?
my_list = [1,2,3]
print("list: ", type(my_list))
sample_dict = {'foo': 1, 'bar': 2}
print("list: ", type(sample_dict.values()))

# dummy dict; think solution is written to work on data passed dynamically
my_dict = {'band1': 47, 'band2': 14, 'band3': 50}


def sort_dict_by_value(dict):

	# unsure how to init empty dict, hence the hack
	sorted_dict = dict.copy()
	sorted_dict.clear()

	# 'for...in' interpolates length of iterable i.e. could just pass my_dict but this more explicit that our concern is the dictionary's length alone
	for x in range(len(my_dict)):
		result = find_dict_high_value(dict)
		sorted_dict[result[0]] = result[1]

	print("sorted dictionary: ", sorted_dict)


def find_dict_high_value(dict):
	high_val = 0
	for key in my_dict.keys():
		current_val = my_dict[key]
		if current_val > high_val:
			high_val = current_val
			high_key = key
	del dict[high_key]
	return [high_key, high_val]


sort_dict_by_value(my_dict)
