# Chapter 1 - Binary search + Big O

Binary search will take log2(n) steps to run in the worst case, whereas a siple search will take n steps. (Whenever log is mentioned in the book, it means log2)

Let's say you have a list of 8 numbers, using binary search it would check 3 numbers at most. I.e. to find 1, you'd first guess 4, then 2, then 1. log2(8) == 3. Simple sarch would check n at worst == 8.

Binary search only works when a list is in sorted order. Hence the too high/too low.

Binary search in Big O notation -> O(log n).

Run times grow at very different speeds! This is why it's not enough to know how long an algorithm takes to run,
you also need to know how the running time increases as the list size increases. -> Big O notation.

If you take linear/simple search in Big O -> O(n). Big O notation lets you compare the **number of operations**, i.e. how fast the algorithm grows. **Reason it's really useful** is if you were comparing two algorithms and for one input it's 15 times faster than the other algorithm, it _doesn't_ mean that it'll be 15 times faster based on another input.

**Big O establishes the worst-case runtime**. Just because you found the item in the first try using simple search doesn't make it O(1). Big O notation is also a reassurance, so for simple search, you know it'll never be slower than O(n)time.

## Key Takeaways:

- Algorithm speed isn't measured in seconds, but in growth of **number of operations**.
- Algorithm times are measured in terms of growth of an algorithm.
- Algorithm times are written in Big O notation.

## The travelling salesperson

Apparently this is an unsolved problem in computer science. Imagine you want to travel the shortest distance possible between a number of cities and you have to visit each one.
If you're visiting 5 cities, there are 120 possible permutations!! Once you're dealing with 100+ cities it's impossible to calculate the answer in time - the sun will collapse first :smile:. Run time -> O(n!)
