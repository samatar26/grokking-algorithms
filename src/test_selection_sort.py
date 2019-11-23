from chapter2 import selection_sort_smallest_to_biggest


def test_selection_sort_smallest_to_biggest():
    assert selection_sort_smallest_to_biggest([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
