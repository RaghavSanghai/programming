num = 5
print(float(num))  # Output: 5.0
print(int(5.7))    # Output: 5
print(str(10))     # Output: "10"

print(type(num))        # Output: <class 'int'>
num= float(num)
print(type(num))       # Output: <class 'float'>

num = "20"
print(type(num))       # Output: <class 'str'>
num = int(num)
print(type(num))       # Output: <class 'int'>

a = 77.85
print(int(a))        # Output: 77
print(str(a))        # Output: "77.85"

s="hello"
print(int(s))        # Raises ValueError
print(float(s))      # Raises ValueError   

