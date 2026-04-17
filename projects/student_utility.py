import math

def calculate_cgpa():
    n = int(input("Enter number of subjects: "))
    total = 0
    
    for i in range(n):
        grade = float(input(f"Enter grade point for subject {i+1}: "))
        total += grade
    
    cgpa = total / n
    print("Your CGPA is:", round(cgpa, 2))


def simple_interest():
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate (%): "))
    t = float(input("Enter Time (years): "))
    
    si = (p * r * t) / 100
    print("Simple Interest is:", si)


def compound_interest():
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate (%): "))
    t = float(input("Enter Time (years): "))
    
    ci = p * (1 + r/100) ** t - p
    print("Compound Interest is:", round(ci, 2))


def area_calculator():
    print("\n1. Circle")
    print("2. Triangle")
    
    choice = input("Choose shape: ")
    
    if choice == '1':
        r = float(input("Enter radius: "))
        area = math.pi * r * r
        print("Area of circle:", round(area, 2))
    
    elif choice == '2':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = 0.5 * b * h
        print("Area of triangle:", area)
    
    else:
        print("Invalid choice")


def main():
    while True:
        print("\n--- Student Utility Menu ---")
        print("1. Calculate CGPA")
        print("2. Simple Interest")
        print("3. Compound Interest")
        print("4. Area Calculator")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            calculate_cgpa()
        elif choice == '2':
            simple_interest()
        elif choice == '3':
            compound_interest()
        elif choice == '4':
            area_calculator()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()