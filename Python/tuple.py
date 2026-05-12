#example: # A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#eg: my_tuple = (1, 2, 3)

t1 = ("Python", 10, 1.5, True, None, [1,2,4], (10,20))
t2 = 10, 20, 30
print(type(t2))  # Output: <class 'tuple'>

l1 = [1, 2, 3]
t3 = tuple(l1)
print(type(t3))  # Output: <class 'tuple'>

fruits = ("apple", "banana", "cherry")
fruits = list(fruits)
print(type(fruits))  # Output: <class 'list'>

