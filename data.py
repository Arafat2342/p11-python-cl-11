row = int(input('Enter the number of row of the right triangle: '))
num = 1

for i in range(1, row + 1):
    for j in range(1, row + 1):
        if j <= row - i:
            print(' ', end="  ")
        else:
            print(num, end="  ")
            num = num + 1
    print() 