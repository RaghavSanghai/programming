'''
a=float(input("Enter the first side of the triangle: "))
b=float(input("Enter the second side of the triangle: "))
c=float(input("Enter the third side of the triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is:",round(area, 3))
''' 

#For right angled triangle
base=float(input("Enter the base of the triangle: "))
height=float(input("Enter the height of the triangle: "))
area=0.5*base*height
print("The area of the triangle is:",round(area, 3))
