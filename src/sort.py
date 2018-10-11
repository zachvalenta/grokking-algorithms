# TODO: dig into 'RuntimeError: dictionary changed size during iteration'
# https://stackoverflow.com/a/18806531/6813490
# TODO: rf away from separate functions


def selection_sort(user_dict):
	sorted_dict = {}
	for _ in range(len(user_dict)):
		k, v = find_high_val(user_dict)
		user_dict.pop(k)
		sorted_dict[k] = v
	return sorted_dict


def find_high_val(dict_at_time):
	high_key = ''
	high_val = 0
	for x in dict_at_time:
		if dict_at_time[x] > high_val:
			high_key = x
			high_val = dict_at_time[x]
	return high_key, high_val
