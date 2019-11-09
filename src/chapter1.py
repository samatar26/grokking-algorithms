# Decorator to test how many calls my binary search funcion makes
def count(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)

    wrapped.calls = 0
    return wrapped


@count
def binary_search(sorted_list, item):
    """
    Find the mid_point index and corresponding item at mid_point index
    if mid_point == item 🎉
    otherwise if list only has that one element return None
    if list has more than 1 element and mid_point item > item return the first half of list
    otherwise return latter half

    """
    mid_point_index = (len(sorted_list) - 1) // 2
    mid_point = sorted_list[(len(sorted_list) - 1) // 2]

    if mid_point == item:
        return mid_point
    elif mid_point_index == 0:
        return None
    elif mid_point > item:
        return binary_search(sorted_list[0:mid_point_index], item)
    else:
        return binary_search(sorted_list[mid_point_index:-1], item)


def binary_search_iterative(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return guess
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
