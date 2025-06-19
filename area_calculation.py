condition = input("Enter the condition: ")
if condition == "s":
    side = int(input("Enter the side of the square: "))
    square = side * side
    print("The area of the square is: ", square)

elif condition == "t":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    triangle = base * height / 2
    print("The area of the triangle is: ", triangle)

elif condition == "r":
    width = int(input("Enter the width of the rectangle: "))
    height2 = int(input("Enter the height of the rectangle: "))
    rectangle = width * height2
    print("The area of the rectangle is: ", rectangle)

else:
    print("Wrong Condition")