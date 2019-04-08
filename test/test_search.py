import src.search as search


def test_simple():
    assert search.simple() <= 100


def test_binary_happy():
    query = 42
    list_happy = [2, 13, 24, 35, 42, 57, 68, 79]
    assert search.binary(query, list_happy) == "found 42"


def test_binary_sad():
    query = 42
    list_unhappy = [2, 13, 24, 35, 46, 57, 68, 79]
    assert search.binary(query, list_unhappy) == "could not find 42"
