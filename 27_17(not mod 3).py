f = open("27_17.txt")
N = int(f.readline())
minim = 10000000
summa = 0

for i in range(N):
    first, second = f.readline().split()
    first = int(first)
    second = int(second)
    if first < second:
        summa += first
    else:
        summa += second
    if abs(first - second) < minim and abs(first - second) % 3 != 0:
        minim = abs(first - second)
if summa % 3 != 0:
    print(summa)
else:
    print(summa + minim)