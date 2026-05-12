#concatenation and repetition of tuples
t1=(3,8,1,0,4,9,7,3,6)
t2=(10,20,30)
print(t1+t2)  # Output: (3, 8, 1, 0, 4, 9, 7, 3, 6, 10, 20, 30)
print(t2+t1)  # Output: (10, 20, 30, 3, 8, 1, 0, 4, 9, 7, 3, 6)
print(t1*2)   # Output: (3, 8, 1, 0, 4, 9, 7, 3, 6, 3, 8, 1, 0, 4, 9, 7, 3, 6)

#in and not in operator is used to check if an element is present or not present in a tuple.
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)  # Output: True
print("kiwi" in fruits)  # Output: False
print("kiwi" not in fruits)  # Output: True
print("banana" not in fruits)  # Output: False

#count() method is used to count the number of occurrences of an element in a tuple.
numbers = (1, 2, 3, 4, 5, 2, 2)
print(numbers.count(2))  # Output: 3
print(numbers.count(6))  # Output: 0 (element not found in the tuple)

#index() method is used to find the index of the first occurrence of an element in a tuple.
print(fruits.index("banana"))  # Output: 1
print(fruits.index("kiwi"))  # Output: ValueError: tuple.index(x): x not found

#min() and max() functions are used to find the minimum and maximum values in a tuple.
numbers = (5, 2, 9, 1, 5, 6)
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9

#sum() function is used to calculate the sum of all the elements in a tuple.
numbers = (5, 2, 9, 1, 5, 6)
print(sum(numbers))  # Output: 28

#reversed() function is used to reverse the elements of a tuple and returns an iterator.
numbers = (5, 2, 9, 1, 5, 6)
reversed_numbers = reversed(numbers)
print(tuple(reversed_numbers))  # Output: (6, 5, 1, 9, 2, 5)

#sorted() function is used to sort the elements of a tuple and returns a new sorted list.
numbers = (5, 2, 9, 1, 5, 6)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]

#len() function is used to find the number of elements in a tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Output: 3

#tuple unpacking is a feature in Python that allows you to assign the elements of a tuple to multiple variables in a single line of code.
fruits = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Output: "apple"
print(fruit2)  # Output: "banana"
print(fruit3)  # Output: "cherry"

#nested tuples are tuples that contain other tuples as elements. You can access the elements of nested tuples using multiple indexing.
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3
print(nested_tuple[2][1])  # Output: 4
