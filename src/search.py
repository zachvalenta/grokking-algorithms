import random


def simple():
    """
    * pg. 5
    * runtime 📈: O(n)
    """
    number_to_guess = random.randint(0, 99)
    accumulated_guesses = 0

    for i in range(0, 100):
        accumulated_guesses = accumulated_guesses + 1
        if i == number_to_guess:
            return accumulated_guesses


def binary(user_search, sorted_list):
    """
    * pg. 6
    * runtime 📈: O(log n)
    * characteristics:

    - requires an ordered list
    - 3 variables to track low/middle/high index in list
    - keep guessing the middle index and reset low/high index as necessary
    """
    low_index = 0
    high_index = len(sorted_list) - 1

    while low_index <= high_index:
        mid = (high_index + low_index) // 2
        if sorted_list[mid] == user_search:
            return 'found {}'.format(user_search)
        elif sorted_list[mid] > user_search:
            high_index = mid - 1
        else:
            low_index = mid + 1

    return 'could not find {}'.format(user_search)
