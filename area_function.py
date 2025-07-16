def square():
    a = int(input("Enter the side: "))
    s = a ** 2
    print("The area is: ", s)

def rectangle():
    a = int(input("Enter the length: "))
    b = int(input("Enter the width: "))
    s = a * b
    print("The area is: ", s)

def triangle():
    a = int(input("Enter the height: "))
    b = int(input("Enter the base: "))
    s = a * b / 2
    print("The area is: ", s)

ch = 1
while ch:
    print("Press 1 for area of a square")
    print("Press 2 for area of a rectangle")
    print("Press 3 for area of a triangle")

    choice = int(input("Make a choice: "))

    if choice == 1:
        square()

    elif choice == 2:
        rectangle()

    elif choice == 3:
        triangle()

    else:
        print("Wrong choice, try again.")
    ch = int(input("Press 0 to stop, else continue"))