f = open("27_19.txt")
N = int(f.readline())
minim = 10000000
sumFin = 0
sumS = 0
sumT = 0
buffer = []
for i in range(N):
    first, second, third = f.readline().split()
    first = int(first)
    second = int(second)
    third = int(third)
    buffer.append(first)
    buffer.append(second)
    buffer.append(third)
    buffer.sort()
    sumFin += buffer[0]
    sumS += buffer[1]
    sumT += buffer[2]
    if (buffer[1]-buffer[0]) <= minim and (buffer[1]-buffer[0]) % 2 == 1:
        minim = buffer[1]-buffer[0]
    elif (buffer[2]-buffer[0]) <= minim and (buffer[2]-buffer[0]) % 2 == 1:
        minim = buffer[2]-buffer[0]
    buffer.clear()
print(minim)
if (sumS + sumT) % 2 != 0:
    print(sumFin)
else:
    print(sumFin + minim)
