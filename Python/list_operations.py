#slicing of lists
l1=[3,8,1,0,4,9,7,3,6]
print(l1[2:5])  # Output: [1, 0, 4]
print(l1[:4])   # Output: [3, 8, 1, 0]
print(l1[5:])   # Output: [9, 7, 3, 6]
print(l1[-3:])  # Output: [7, 3, 6]

#concatenation and repetition of lists
l2=[10,20,30]
print(l1+l2)  # Output: [3, 8, 1, 0, 4, 9, 7, 3, 6, 10, 20, 30]
print(l2+l1)  # Output: [10, 20, 30, 3, 8, 1, 0, 4, 9, 7, 3, 6]
print(l1*2)   # Output: [3, 8, 1, 0, 4, 9, 7, 3, 6, 3, 8, 1, 0, 4, 9, 7, 3, 6]

#appending and extending lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.extend(["grape", "melon"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'melon']

#inserting and removing and popping elements from lists
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange', 'grape', 'melon']
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange', 'grape', 'melon']
fruits.pop(2)
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape', 'melon']
fruits.pop()  # removes the last element
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape']   
fruits.pop(2)  # removes the element at index 2
print(fruits)  # Output: ['apple', 'kiwi', 'grape']
fruits.remove("kiwi","orange")  # Output: TypeError: remove() takes exactly one argument (2 given)
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape'] (original list remains unchanged)
fruits.append("kiwi","orange")  # Output: TypeError: append() takes exactly one argument (2 given)
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape'] (original list remains unchanged)
fruits.append("kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape', 'kiwi']
fruits.remove("kiwi")
print(fruits)  # Output: ['apple', 'orange', 'grape', 'kiwi'] (only the first occurrence of 'kiwi' is removed)

#reverse() and sort() methods
numbers = [5, 2, 9, 1, 5, 6]
numbers.reverse()
print(numbers)  # Output: [6, 5, 1, 9, 2, 5]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]    

#count() method is used to count the number of occurrences of an element in a list.
numbers = [1, 2, 3, 4, 5, 2, 2]
print(numbers.count(2))  # Output: 3
print(numbers.count(6))  # Output: 0 (element not found in the list)

#in not in operator is used to check if an element is not present in a list.
fruits = ["apple", "banana", "cherry"]
print("kiwi" not in fruits)  # Output: True
print("banana" not in fruits)  # Output: False

#min() and max() functions are used to find the minimum and maximum values in a list.
numbers = [5, 2, 9, 1, 5, 6]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9
print(min(fruits))  # Output: apple (based on alphabetical order)
print(max(fruits))  # Output: cherry (based on alphabetical order)
print(numbers.min())  # Output: AttributeError: 'list' object has no attribute 'min'
print(numbers.max())  # Output: AttributeError: 'list' object has no attribute 'max'

#sum() function is used to calculate the sum of all elements in a list.
numbers = [5, 2, 9, 1, 5, 6]
print(sum(numbers))  # Output: 28
print(sum(fruits))  # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str' (you cannot sum a list of strings)
