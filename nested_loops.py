f = 5

for i in range(5,0,-1):
    f = f - 1
    for j in range(i):
        print(f, end = " ")
    print()