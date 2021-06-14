f = open("23_B.txt")
N = int(f.readline())
summa = 0
arr0 = [100000]*3
arr1 = [100000]*3
arr2 = [100000]*3
for i in range(N):
    num = f.readline()
    num = int(num)

    if num % 3 == 0:
        if num <= arr0[0]:
            arr0[2] = arr0[1]
            arr0[1] = arr0[0]
            arr0[0] = num
        elif num <= arr0[1]:
            arr0[2] = arr0[1]
            arr0[1] = num
        elif num <= arr0[2]:
            arr0[2] = num

    if num % 3 == 1:
        if num <= arr1[0]:
            arr1[2] = arr1[1]
            arr1[1] = arr1[0]
            arr1[0] = num
        elif num <= arr1[1]:
            arr1[2] = arr1[1]
            arr1[1] = num
        elif num <= arr1[2]:
            arr1[2] = num

    if num % 3 == 2:
        if num <= arr2[0]:
            arr2[2] = arr2[1]
            arr2[1] = arr2[0]
            arr2[0] = num
        elif num <= arr2[1]:
            arr2[2] = arr2[1]
            arr2[1] = num
        elif num <= arr2[2]:
            arr2[2] = num
min0 = sum(arr0)
min1 = sum(arr1)
min2 = sum(arr2)
minmix = arr0[0] + arr1[0] + arr2[0]
print(min(min0, min1, min2, minmix))
