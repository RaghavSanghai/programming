#Sets are non-indexed, meaning that you cannot access elements in a set using an index.
#Sets are unordered collections of unique elements. 
#They are mutable, meaning that you can add or remove elements from a set after it has been created. 
#Sets are defined using curly braces {} or the built-in set() function.
#Example of a set:
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

#sets do not allow duplicate elements. If you try to add a duplicate element to a set, it will be ignored.
my_set.add(3)
print(my_set)  # Output: {1, 3, 4} (the duplicate element 3 is ignored) 
s1 = {1, 2, 3, 4, 4,9}
print(s1)  # Output: {1, 2, 3, 4, 9} (the duplicate element 4 is ignored)

#sets can be used when the values are unique and you want to eliminate duplicates. Example: passport numbers, email addresses, etc.
