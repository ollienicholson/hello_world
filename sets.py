# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets cannot have two items with the same value.
# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)
# print(len(thisset))
# print(type(thisset))
# print(list(thisset))
# print(dict(thisset)) # Error: K-V pair is required
# print(str(thisset))
# print(tuple(thisset))

my_list = [1, 2, 3, 4, 1, 2, 5, 6]
unique_elements = set(my_list)
# print(unique_elements)

my_set = set([1, 2, 3, 4, 5])
if 3 in my_set:
    print("3 is present in the set")

set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

# Union
union = set1.union(set2)
print(union, ">> union")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
intersection = set1.intersection(set2)
print(intersection, ">> intersection")  # Output: {4, 5}

# Difference
difference = set1.difference(set2)
print(difference, ">> diff")  # Output: {1, 2, 3}

# Symmetric difference
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference, ">> sym diff")  # Output: {1, 2, 3, 6, 7, 8}

new_set = set([1, 2, 3, 4, 5])
new_set.remove(3)
print(new_set, ">> remove")  # Output: {1, 2, 4, 5}

# ============================================================================

# ---->>> so when is it not suitable to use the set function???

# While sets are a powerful and useful data structure in Python, there are some situations where using sets may not be suitable or efficient. Here are some scenarios where sets may not be the best option:

# Ordering: Sets in Python are unordered. If you need to maintain the order of elements, you should use a different data structure like a list or a tuple.

# Duplicate elements: Sets automatically remove duplicates from a collection. If you need to keep duplicates in the collection, you should use a different data structure like a list.

# Memory usage: Sets use more memory than lists for small collections of elements. If you have a small collection of elements, it may be more efficient to use a list or a tuple instead of a set.

# Performance: While sets have constant-time membership testing, their performance can degrade if there are many collisions. If you are working with very large collections of elements or if you have a lot of collisions, it may be more efficient to use a different data structure like a hash table or a binary search tree.

# Immutability: Sets in Python are mutable, which means you can modify them in-place. If you need an immutable collection of elements, you should use a different data structure like a tuple or a frozen set.

# In summary, while sets are a versatile and powerful data structure in Python, they may not be the best choice for every situation. It's important to consider the specific needs of your application when choosing a data structure.

# ============================================================================

#  == Alternative data structures ==

# Python has several alternative data structures to lists and sets, including:

# Tuples: Tuples are similar to lists, but they are immutable, which means you can't modify them in-place. Tuples are often used for fixed-size collections of elements, like coordinates or dates.

# Dictionaries: Dictionaries are another hash table-based data structure that allows you to store key-value pairs. Dictionaries provide constant-time access to values based on their keys, making them useful for lookups and indexing.

# Namedtuples: Namedtuples are a subclass of tuples that have named fields, which makes them more readable and easier to use in some contexts. Namedtuples are often used to represent records or data points.

# Queues: Queues are a data structure that allows you to add and remove elements in a first-in, first-out (FIFO) order. Queues are useful for implementing algorithms that require a FIFO order, like breadth-first search.

# Stacks: Stacks are a data structure that allows you to add and remove elements in a last-in, first-out (LIFO) order. Stacks are useful for implementing algorithms that require a LIFO order, like depth-first search.

# Deques: Deques are a data structure that allows you to add and remove elements from either end in constant time. Deques are useful for implementing algorithms that require efficient insertion and deletion at both ends, like sliding window algorithms.

# Heap: Heap is a binary tree-based data structure that allows you to add and remove elements in logarithmic time. Heap is useful for maintaining a collection of elements that need to be partially ordered, like finding the k-th smallest or largest element in a collection.

# These alternative data structures provide different trade-offs in terms of performance, memory usage, and functionality, and choosing the right one depends on the specific requirements of your application.