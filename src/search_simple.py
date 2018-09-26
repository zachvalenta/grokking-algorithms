"""
source: Grokking Algorithms [pg. k5]
runtime: O(n)
"""

import random


def simple_search():

	number_to_guess = random.randint(1, 100)
	accumulated_guesses = 0

	for i in range(101):
		accumulated_guesses = accumulated_guesses + 1
		if i == number_to_guess:
			return accumulated_guesses
