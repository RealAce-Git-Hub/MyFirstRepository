#non-parameterized function to find the area of a square with return
def area_of_square1():
    a = int(input("Enter the side of the square: "))
    s = a * a
    return s

#paramaeterized function to find the area of a square with return
def area_of_square2(a):
    area = a * a
    return area

#non-paramaeterized function to find the area of a square without return

def area_of_square3():
    a = int(input("Enter the side of the square: "))
    s = a*a
    print("The area of the square is ",s)

#paramaeterized function to find the area of a square without return

def area_of_square4(a):
    s = a * a
    print("The are of the square is",s)

######## non-parameterized with return
print("-"*5,"Non-parameterized Function to find the area of the square with return","-"*5)
result1 = area_of_square1()
print("The area of the square is for function1",result1)

######## parameterized with return
print("-"*5,"Parameterized Function to find the area of the square with return","-"*5)
side = int(input("Enter the side of the square: "))
result2 = area_of_square2(side)
print("The area of the square is",result2)

####### non-parameterized without return
print("-"*5,"Non-Parameterized Function to find the area of the square without return","-"*5)
area_of_square3()

####### parameterized without return
a = int(input("Enter the side of the square: "))
print("-"*5,"Parameterized Function to find the area of the square without return","-"*5)
area_of_square4(a)