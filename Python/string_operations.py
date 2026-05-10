s1="Python"
print(s1[0])  # Output: P
print(s1[-1])  # Output: n
print(s1[2:5])  # Output: tho
print(len(s1))  # Output: 6
print(s1.split("y"))  # Output: ['P', 'thon']
version="3.8.5"
print(version.split("."))  # Output: ['3', '8', '5']
print(s1 * 3)  # Output: PythonPythonPython
print(s1 + version)  # Output: Python3.8.5
print(s1 - version)  # Output: TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("yth" in s1)  # Output: True
print("java" in s1)  # Output: False
print("z" not in s1)  # Output: True

print("Python" == "Python")  # Output: True
print("Python" == "python")  # Output: False
print("Python " == "Python")  # Output: False

#strip() method is used to remove any leading and trailing whitespace from a string.
s2="   Hello, World!   "
print(s2.strip())  # Output: Hello, World!
print(s2)  # Output:    Hello, World!   (original string remains unchanged

#replace() method is used to replace a specified phrase with another specified phrase.
text = "Hello, World!"
print(text)
print(text.replace("World", "Python"))  # Output: Hello, Python!
print(text)  # Output: Hello, World! (original string remains unchanged)
print(text.replace("o", "0"))  # Output: Hell0, W0rld!
print(text.replace("l", "L", 2))  # Output: HeLLo, World! (only the first 2 occurrences of 'l' are replaced)

#count() method is used to count the number of occurrences of a substring in a string.
txt="We are learning Python. Python is fun."
print(txt.count("Python"))  # Output: 2
print(txt.count("python"))  # Output: 0 (case-sensitive)

#Changing case of a string
s1="Python"
print(s1.upper())  # Output: PYTHON
print(s1.lower())  # Output: python
print(s1.capitalize())  # Output: Python
print(s1.title())  # Output: Python

#starting and ending of a string: startswith() and endswith() methods are used to check if a string starts or ends with a specified substring.
s1="Python programming"
print(s1.startswith("Python"))  # Output: True
print(s1.endswith("programming"))  # Output: True
print(s1.startswith("programming"))  # Output: False
print(s1.endswith("Python"))  # Output: False
