'''
Sports competition. The participants involved are divided into various groups based on their height.
E: 145cm to 155cm
D: 156cm to 160cm
C: 161cm to 175cm
B: 176cm to 180cm
A: 181cm to 190cm
'''

height_of_the_participant = int(input("Enter your height: "))

if (height_of_the_participant >= 181) and (height_of_the_participant <=190):
    print("You belong to group A")

elif (height_of_the_participant >= 176) and (height_of_the_participant <=180):
    print("You belong to group B")
    
elif (height_of_the_participant >= 161) and (height_of_the_participant <=175):
    print("You belong to group C")

elif (height_of_the_participant >= 156) and (height_of_the_participant <=160):
    print("You belong to group D")

elif (height_of_the_participant >= 145) and (height_of_the_participant <=155):
    print("You belong to group E")

else:
    print("You cannot participate. Your height is out of the range.")