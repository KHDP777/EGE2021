f = open("27_17.txt")
N = int(f.readline())
ost1M = 10000000
ost1P = 10000000
ost2M = 10000000
ost2P = 10000000
summa = 0
for i in range(N):
    first, second = f.readline().split()
    first = int(first)
    second = int(second)
    if first < second:
        summa += first
    else:
        summa += second

    if abs(first - second) <= ost1M and abs(first - second) % 3 == 1:
        ost1P = ost1M
        ost1M = abs(first - second)
    else:
        if abs(first - second) < ost1P and abs(first - second) % 3 == 1:
            ost1P = abs(first - second)

    if abs(first - second) <= ost2M and abs(first - second) % 3 == 2:
        ost2P = ost2M
        ost2M = abs(first - second)
    else:
        if abs(first - second) < ost2P and abs(first - second) % 3 == 2:
            ost2P = abs(first - second)
print(summa, summa % 3, ost1M, ost1P, ost2M, ost2P)
if summa % 3 == 0:
    print(summa)
elif summa % 3 == 1:
    if ost2M < ost1M + ost1P:
        print(summa + ost2M)
    else:
        print(summa + ost1M + ost1P)
elif summa % 3 == 2:
    if ost1M < ost2M + ost2P:
        print(summa + ost1M)
    else:
        print(summa + ost2M + ost2P)
