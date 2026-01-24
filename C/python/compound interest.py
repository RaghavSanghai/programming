p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time (in years): "))
ci=(p*((1+r/100)**t))-p
print("The compound interest is:",round(ci, 2))
