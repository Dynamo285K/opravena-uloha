def triangle(riadky):
    for i in range(riadky):
        for r in range(riadky-i-1):
            print(end=" ")
        for r in range(i+1):
            print('*',end=" ")
        print()
triangle(5)
