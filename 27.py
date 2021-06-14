f = open("27_B.txt")
N = int(f.readline())
summa = 0
minim = 100000
arr = []
for i in range(N):
    first, second, third = f.readline().split()
    first = int(first)
    second = int(second)
    third = int(third)
    summa += max(first, second, third)
    if (minim > abs(first - second)) and (abs(first - second) % 109) != 0:
        minim = abs(first - second)
    if (minim > abs(first - third)) and (abs(first - third) % 109) != 0:
        minim = abs(first - third)
    if (minim > abs(third - second)) and (abs(third - second) % 109) != 0:
        minim = abs(third - second)
    arr.append(minim)
print(summa, minim)
if summa % 109 != 0:
    print(summa)
else:
    print(summa - minim)

