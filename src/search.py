from collections import deque
import random


def simple():
    number_to_guess = random.randint(0, 99)
    accumulated_guesses = 0
    for i in range(0, 100):
        accumulated_guesses = accumulated_guesses + 1
        if i == number_to_guess:
            return accumulated_guesses


def binary(user_search, sorted_list):
    """
    📙 6
    📈 O(log n)
    - requires an ordered list
    - 3 variables to track low/middle/high index in list
    - keep guessing the middle index
    - reset low/high index as necessary to chop list in half each time
    - breaks if indices in billions
        🔗 https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
    """
    low_index = 0
    high_index = len(sorted_list) - 1

    while low_index <= high_index:
        mid = (high_index + low_index) // 2
        if sorted_list[mid] == user_search:
            return "found {}".format(user_search)
        elif sorted_list[mid] > user_search:
            high_index = mid - 1
        else:
            low_index = mid + 1

    return "could not find {}".format(user_search)


def bfs(graph, condition):
    """
    📙 110
    📈 O(num of edges)
    - graph = map of lists
    - take root K and handle each V
    - handle = yes (exit) no (use V as K and enque its V)
    """
    queue = deque(graph['root'])
    while queue:
        current = queue.popleft()
        if current is condition:
            return True
        else:
            try:
                queue += graph[current]
            except KeyError:
                pass
    return False
