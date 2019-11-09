# Chapter 1 - Binary search + Big O
Binary search will take log2(n) steps to run in the worst case, whereas a siple search will take n steps. (Whenever log is mentioned in the book, it means log2)

Let's say you have a list of 8 numbers, using binary search it would check 3 numbers at most. I.e. to find 1, you'd first guess 4, then 2, then 1. log2(8) == 3. Simple sarch would check n at worst == 8.

Binary search only works when a list is in sorted order. Hence the too high/too low.