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

x = "pie"
y = 3.14
print (x + y)   # Raises TypeError
print (x + str(y))  # Output: "pie3.14"

p = "10"
q = "2.5"
print (p + q)        # Output: "102.5"
print (int(p) + float(q))  # Output: 12.5


