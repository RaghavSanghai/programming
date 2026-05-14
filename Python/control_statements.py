#if statement:
"""syntax:
if condition:
    statement 1
    statement 2
    ...
    statement n
statement x
"""
age = float(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
print("Thank you for using the voting system.")

#if-else statement:
"""syntax:
if condition:
    block of code to be executed if the condition is true
else:
    block of code to be executed if the condition is false
"""
age = float(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#if-elif-else statement:
"""syntax:
if condition1:
    block of code to be executed if the condition is true
elif condition2:
    block of code to be executed if the condition2 is true
else:
    block of code to be executed if both conditions are false
"""

marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
elif marks >= 50 and marks < 60:
    print("Grade: E")
else:
    print("Grade: F")

# Nested if statement
"""syntax:
if condition1:
    if condition2:
        block of code to be executed if both conditions are true
    else:
        block of code to be executed if condition1 is true and condition2 is false
else:
    block of code to be executed if condition1 is false
"""
age = float(input("Enter your age: "))
if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

# Ternary operator (conditional expression)
"""syntax:
variable = value_if_true if condition else value_if_false
"""
age = float(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print("You are an", status)