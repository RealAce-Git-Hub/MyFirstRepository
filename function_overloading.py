#function to find the area of the square
def area(s, name = "first_function"):
    area = s * s
    print("Area of the square: ", area)

#function to find the area of a rectangle
def area(l, b, name = "second_function",):
    area = l * b
    print("Area of the rectangle: ", area)

if __name__ == "__main__":
    sq = int(input("Enter the side of square: "))
    area (sq)
    length = int(input("Enter the length of rectangle: "))
    breadth = int(input("Enter the breadth of rectangle: "))
    area(length, breadth)