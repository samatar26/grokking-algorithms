import pytest
from math import log2
from src.chapter1 import binary_search, binary_search_iterative


def test_binary_search_succesful():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
    item = 1
    assert binary_search(sorted_list, item) == 1
    assert binary_search.calls == 3


def test_binary_search_unsuccesful():
    binary_search.calls = 0  # Super hacky reset calls between tests
    sorted_list = [1, 2, 3, 4]
    item = 0
    assert binary_search(sorted_list, item) == None
    assert binary_search.calls == log2(len(sorted_list))


def test_binary_search_unsuccesful_single_element():
    binary_search.calls = 0  # Super hacky reset calls between tests
    sorted_list = [1]
    item = 100
    assert binary_search(sorted_list, item) == None
    assert binary_search.calls == 1


def test_binary_search_iterative():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
    item = 1

    assert binary_search_iterative(sorted_list, item) == 1
