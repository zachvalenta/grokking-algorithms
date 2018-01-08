"""
runtime: O(n)
"""


num_that_ur_trying_to_guess = 42


def simple_search():

	num_uv_already_guessed = []

	for index in range(100):
		if index == num_that_ur_trying_to_guess:
			break
		else:
			num_uv_already_guessed.append(index)

	print(num_uv_already_guessed)


simple_search()
