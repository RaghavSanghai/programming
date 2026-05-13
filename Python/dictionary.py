#Dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure in Python. 
#Each key in a dictionary must be unique and immutable, while the values can be of any data type and can be duplicated.
#Dictionaries are defined using curly braces {} and key-value pairs are separated by a colon :.
#Example of a dictionary:
groceries = {"milk":60, "biscuits":20, "rice":90, "bread":30}
print(groceries)  # Output: {'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 30}
print(len(groceries))  # Output: 4 (number of key-value pairs in the dictionary)
print(groceries["milk"])  # Output: 60 (accessing the value associated with the key "milk")
groceries["eggs"] = 50  # Adding a new key-value pair to the dictionary
print(groceries[0])  # Output: Error: KeyError: 0 (dictionaries are not indexed by position, they are accessed by keys)
print(groceries)  # Output: {'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 30, 'eggs': 50}
groceries["milk"] = 65  # Modifying the value associated with the key "milk"
print(groceries)  # Output: {'milk': 65, 'biscuits': 20, 'rice': 90, 'bread': 30, 'eggs': 50}
del groceries["biscuits"]  # Removing the key-value pair with the key "biscuits"
print(groceries)  # Output: {'milk': 65, 'rice': 90, 'bread': 30, 'eggs': 50}