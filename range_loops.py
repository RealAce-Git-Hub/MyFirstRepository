f = 5

for i in range(5,0,-1):
    for j in range(i):
        f = f - 1
        print(f + 1, end = " ")
    print()