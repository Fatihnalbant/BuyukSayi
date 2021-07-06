'''def getmax(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c


x = getmax(78, 24, 5)
print(x)
'''

def getmax(a, b, c):
    return (a if a > c else c) if a > b else (b if b > c else c)


x = getmax(12, 98, 5)
print(x)
