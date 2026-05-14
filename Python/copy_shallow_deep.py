import copy

#shallow copy
l1 = [1, 2.5, [10,20,30], "Python"]
l2 = copy.copy(l1)
print(l1)  # Output: [1, 2.5, [10, 20, 30], 'Python']
print(l2)  # Output: [1, 2.5, [10, 20, 30], 'Python']
print(l1 is l2)  # Output: False (l1 and l2 are different objects in memory)
print(l1[2] is l2[2])  # Output: True (the nested list [10, 20, 30] is the same object in both l1 and l2, because shallow copy creates a new outer list but does not create new inner objects)

l1[0] = 5
l1[2][0] = 50
print(l1)  # Output: [5, 2.5, [50, 20, 30], 'Python'] (the first element of l1 is changed to 5 and the first element of the nested list is changed to 50)
print(l2)  # Output: [1, 2.5, [50, 20, 30], 'Python'] (the first element of l2 remains unchanged as 1, but the first element of the nested list is changed to 50 because both l1

#deep copy
li=[1,2.5,[10,20,30],"Python"]
li2=copy.deepcopy(li)
print(li)  # Output: [1, 2.5, [10, 20, 30], 'Python']
print(li2)  # Output: [1, 2.5, [10, 20, 30], 'Python']
print(li is li2)  # Output: False (li and li2 are different objects in memory)
print(li[2] is li2[2])  # Output: False (the nested list [10, 20, 30] is a different object in both li and li2, because deep copy creates new objects for all nested objects)

li[0] = 5
li[2][0] = 50
print(li)  # Output: [5, 2.5, [50, 20, 30], 'Python'] (the first element of li is changed to 5 and the first element of the nested list is changed to 50)
print(li2)  # Output: [1, 2.5, [10, 20, 30], 'Python'] (the first element of li2 remains unchanged as 1 and the nested list remains unchanged as [10, 20, 30] because deep copy creates new objects for all nested objects
