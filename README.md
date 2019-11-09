# Grokking Algorithms: An illustrated guide for programmers and other curious people

Notes and exercises following the book :nerd_face:

(!find out more) - Things I need to look a little more into

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

# Chapter 2

## Arrays vs linked lists

Using an array means all your items are stored contiguously (right next to each other) in memory.
The problem arises when you want to add another item to the array and the next spot in memory is taken,
this means the entire array will have to move to a different chunk of memory.
Therefore inserting new elements into an array can be a problem. A potential workaround
(which is definitely not the perfect solution) is to ask the computer to hold extra memory slots just in case.
The problem is your array may not need these extra slots of memory and no-one else can use them.
You may need a bigger chunk of memory than you asked for and will have to move to another location in memory anyway.

In come linked lists :smile:

With linked lists your items can be anywhere in memory. This is because each item stores the address of the next
item in the list. So you go the first item/address in memory and this will tell you where second item is located etc.
Adding an item to a link list is also really easy, because you stick it anywhere in memory with the memory address of the previous item.
Meaning that with linked lists you never have to move your items. **Another benefit** is let's say you're trying to create a list of 10,000 items.
And your memory has 10,000 slots available, but not contiguously, meaning you can't get space for an array!
But this isn't an issue with linked lists as the items are split up anyway, therefore as long as there's space in memory you have space for a linked list.

The downside of a linked list however is the (random) reading time. Suppose you want to find the last item in an array,
because there stored right next to eachother in memory, you can easily find the last item of the array, because
suppose your array starts at address 00 and it's got 5 items, you know the last item is at address 05.
With linked lists, your items are scatterred all over memory and you would need to start at the first element,
ask where the second is until you reach the last one.

Apparently linked lists do well on reads too and only have a problem accessing random elements in the list.
(!find out more)

## Little summary of reading vs insertion vs deletion

So reading:

- Array O(1)
- Linked list O(n)

Insertion:

- Array O(n)
- Linked list O(1)

Deletion:

- Array O(n)
- Linked list O(1)

Insertion and deletion is only O(1) if you can instantly access the element to be deleted.
Common practice is to keep track of the first and last items in a linked list. (!find out more)

Arrays allow **random access** whereas linked lists allow **sequential access**

## Insertion

Suppose you need to insert an element into the middle of a list. When inserting it into a linked list, it's as easy as changing what the previous elements points to.
Whereas with an array you need shift all the rest of the elements down a space in memory and worse yet, if there's no space, it'll have to to copy everything to a new location!

## Deletion

Again linked lists are better as you just need to change what the previous element pointed to. With arrays everything needs to be moved up.
Unlike insertions, deletions will always work, because insertions can fail if there's no more space left in memory,
but you can always delete!
