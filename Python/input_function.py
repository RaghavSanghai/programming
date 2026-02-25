name="Mark"

first_name=input("Enter your first name: ")
print("Hello", first_name)

num1=input("Enter first number: ")
num2=input("Enter second number: ")
sum= num1 + num2
print("The sum is:", sum)  # This will concatenate the inputs as strings
# To perform addition, we need to convert the inputs to integers
sum=int(num1) + int(num2)
print("The sum after converting to integers is:", sum)

#OR we can take the number inputs as integers directly
num3=int(input("Enter third number: "))
num4=int(input("Enter fourth number: "))
sum2= num3 + num4
print("The sum of third and fourth number is:", sum2)

