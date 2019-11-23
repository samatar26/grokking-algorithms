# Exercise 2.1: Linked list! (For lots of insertions vs reads)
"""
 Exercise 2.2:
 Linked list - Because lost of inserts are happening which linked lists excel at.
 And the chefs always take (read) the first order of the queue.
"""
"""
 Exercise 2.3:
 Sorted Array - Because binary search requires access to middle of list, i.e. random access.

 Exercise 2.4:
 Downside of array for inserts is that its runtime is O(n), the reason being that the array items are stored
 contigious in memory. Since we're using binary search, we need a sorted array and therefore suppose we add someone named Adel.
 Their name will be added to the end of the array and therefore we'd have to sort the array everytime a new name is inserted!

 Exercise 2.5:
 Would a hybrid data structure of arrays containing linked lists be faster or slower than arrays/linked lists?
 For searching ->
 It will be slower than using an array. This is because even though you know the first letter,
 to find the exact name you would have to traverse the linked list which is O(n).

 It will be faster than using a linked list as you at least know which part of the sorted list you're looking for
 and can therefore make use of the random access of arrays.

 For insertion ->
 It'll be faster than using an array, since you don't need to insert an entry into the array itself, but into the linked list,
 which is an item of the array.

 It'll be the same as using a linked list.
"""


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort_smallest_to_biggest(arr):
    sorted_arr = []

    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_index))

    return sorted_arr
