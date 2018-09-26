"""
page 9

runtime: O(log n)

FLOW
* query == value at middle index?
* if yes: done
* else:
1) slice everything lower than low guess, reset low to 1 above previous low
2) slice everything higher than high guess, reset high to 1 below previous high

OTHER POINTS
* slice function eliminates half list w/ each guess
* only works on sorted list

"""

hard_code_list = [3, 14, 15, 57, 61, 64, 79, 84, 90, 99]


def create_list():
	one_hundred = []
	for index in range(100):
		one_hundred.append(index)
	return one_hundred


def binary_search():
	magic_number = 99
	list_to_search = create_list()

	low_index = 0
	high_index = len(list_to_search) - 1
	found_yet = False

	while low_index <= high_index:
		mid_index = (high_index + low_index) // 2
		ur_guess = list_to_search[mid_index]
		if ur_guess == magic_number:
			print("found it")
			found_yet = True
			break
		elif ur_guess < magic_number:
			print("too low")
			low_index = mid_index + 1
		else:
			print("too high")
			high_index = mid_index - 1

	if not found_yet:
		print("didn't find")


binary_search()
