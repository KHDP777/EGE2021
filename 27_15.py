f = open("27_15.txt")
N = int(f.readline())
ost120 = [0]*120
pm = 0
for i in range(N):
    num = f.readline()
    num = int(num)
    if num % 120 == 0:
        if ost120[0] <= num:
            pm = ost120[0]
            ost120[0] = num
    else:
        if ost120[num % 120] < num:
            ost120[num % 120] = num

maxS = 0

for i in range(1, 61):
    if ost120[i] + ost120[120-i] >= maxS:
        maxS = (ost120[i] + ost120[120-i])
        first = ost120[i]
        second = ost120[120-i]
        n1= i
        n2 = 120-i



for i in range(120):
    if 9991 == ost120[i] or 9689 == ost120[i]:
        print('!!!!!!!!!!', i)
    print(i, ost120[i])

if ost120[0] + pm > maxS:
    print(ost120[0], pm)
else:
    print(first, second)
    print(n1, n2)