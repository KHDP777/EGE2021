def f(x, y, w):
    if x + y >= 77 and w == 3:
        return True
    else:
        if x + y < 77 and w == 3:
            return False
    return f(x+1, y, w+1) or f(x*2, y, w+1)\
           or f(x, y+1, w+1) or f(x, y*2, w+1)
for s in range(1, 69+1):
    if f(7, s, 1):
        print(s)
        break