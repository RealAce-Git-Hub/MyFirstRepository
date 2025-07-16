def addition():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    s = a + b
    print("The sum is: ", s)

def subtraction():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    s = a - b
    print("The difference is: ", s)

def multiplication():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    s = a * b
    print("The product is: ", s)

def division():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    s = a / b
    print("The quotient is: ", s)

ch = 1
while ch:
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")

    choice = int(input("Make a choice: "))

    if choice == 1:
        addition()

    elif choice == 2:
        subtraction()

    elif choice == 3:
        multiplication()

    elif choice == 4:
        division()

    else:
        print("Wrong choice, try again.")
    ch = int(input("Press 0 to stop, else continue"))