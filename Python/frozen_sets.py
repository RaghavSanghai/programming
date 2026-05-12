#Frozen Sets are similar to sets, but are immutable, meaning, you can't add or remove elements from a frozen set after it has been created.
#Frozen sets are defined using the built-in frozenset() function.
#Example of a frozen set:
my_frozenset = frozenset({1, 2, 3})
print(my_frozenset)  # Output: frozenset({1, 2, 3})
my_frozenset.add(4)  # Output: Error: AttributeError: 'frozenset' object has no attribute 'add' (you cannot add elements to a frozen set)
my_frozenset.remove(2)  # Output: Error: AttributeError: 'frozenset' object has no attribute 'remove' (you cannot remove elements from a frozen set)
