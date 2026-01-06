x = 10 
y = x + 5       # y, x are varialbles, 15 is value, =, + are operators  and variables and value are operator

# Arithmetic Operators
a = 15
b = 4
c = a + b       # c is a variable, 19 is a value, + is an operator
d = a - b       # d is a variable, 11 is a value, - is an operator
e = a * b       # e is a variable, 60 is a value, * is an operator
f = a / b       # f is a variable, 3.75 is a value, / is an operator
g = a % b       # g is a variable, 3 is a value, % is an operator
h = a ** b      # h is a variable, 50625 is a value,
i = a // b      # i is a variable, 3 is a value, // is an operator

# Comparison Operators
x = 10
y = 20
print(x == y)   # Output: False, == is an operator
print(x != y)   # Output: True, != is an operator
print(x > y)    # Output: False, > is an operator
print(x < y)    # Output: True, < is an operator
print(x >= y)   # Output: False, >= is an operator
print(x <= y)   # Output: True, <= is an operator   

# Logical Operators
a = True
b = False
print(a and b)  # Output: False, and is an operator
print(a or b)   # Output: True, or is an operator
print(not a)    # Output: False, not is an operator

# Assignment Operators
x = 5           # = is an operator
x += 3          # x = x + 3, += is an operator
x -= 2          # x = x - 2, -= is an operator
x *= 4          # x = x * 4, *= is an operator
x /= 2          # x = x / 2, /= is an operator
x %= 3          # x = x % 3, %= is an operator
x **= 2         # x = x ** 2, **= is an operator
x //= 3         # x = x // 3, //= is an operator

# Bitwise Operators
a = 10          # In binary: 1010
b = 4           # In binary: 0100
print(a & b)    # Output: 0, & is an operator
print(a | b)    # Output: 14, | is an operator
print(a ^ b)    # Output: 14, ^ is an operator
print(~a)       # Output: -11, ~ is an operator
print(a << 2)   # Output: 40, << is an operator
print(a >> 2)   # Output: 2, >> is an operator  

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # Output: True, in is an operator
print(6 not in my_list)  # Output: True, not in is an operator

# Identity Operators
x = 10
y = 10
print(x is y)        # Output: True, is is an operator
print(x is not y)    # Output: False, is not is an operator
a = [1, 2, 3]
b = a
print(a is b)        # Output: True, is is an operator
print(a is not b)    # Output: False, is not is an operator
c = [1, 2, 3]
print(a is c)        # Output: False, is is an operator
print(a is not c)    # Output: True, is not is an operator

# Operator Precedence
x = 10 + 5 * 2      # Multiplication has higher precedence than addition
y = (10 + 5) * 2    # Parentheses have the highest precedence
z = 10 > 5 and 3 < 7  # Comparison operators have higher precedence than logical operators
print(x)  # Output: 20
print(y)  # Output: 30
print(z)  # Output: True

# Combining Different Operators
a = 5
b = 10
c = 15
result = (a + b) * c / (b - a)  # Combining arithmetic operators
print(result)  # Output: 75.0
flag = (a < b) and (b < c)  # Combining comparison and logical operators
print(flag)  # Output: True

# Unary Operators
x = 5
y = -x          # Unary negation
z = +x          # Unary plus
print(y)  # Output: -5
print(z)  # Output: 5
x = True
y = not x       # Unary logical negation
print(y)  # Output: False

# Ternary Operator
a = 10
b = 20
max_value = a if a > b else b  # Ternary conditional operator
print(max_value)  # Output: 20

# Binary Operators
x = 10
y = 5
sum_value = x + y  # Binary addition operator
diff_value = x - y  # Binary subtraction operator
print(sum_value)   # Output: 15
print(diff_value)  # Output: 5
