def addition(a,b):
    s = a + b
    print("The sum is: ", s)

def subtraction(a,b):
    s = a - b
    print("The difference is: ", s)

def multiplication(a,b):
    s = a * b
    print("The product is: ", s)

def division(a,b):
    s = a / b
    print("The quotient is: ", s)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

ch = 1
while ch:
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")

    choice = int(input("Make a choice: "))

    if choice == 1:
        addition(a,b)

    elif choice == 2:
        subtraction(a,b)

    elif choice == 3:
        multiplication(a,b)

    elif choice == 4:
        division(a,b)

    else:
        print("Wrong choice, try again.")
    ch = int(input("Press 0 to stop, else continue"))