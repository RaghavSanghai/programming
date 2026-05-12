#lists, dictionaries, sets are mutable
#tuples, strings, frozensets are immutable

#mutable means that the object can be modified after it is created, while immutable means that the object cannot be modified after it is created.
#Example of mutable object (list):
my_list = [1, 2, 3]
print(my_list)  # Output: [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

#Example of immutable object (tuple):
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
# my_tuple.append(4)  # This will raise an AttributeError because tuples do not have an append method
# my_tuple[0] = 10  # This will raise a TypeError because tuples do not support item assignment

