

c = 12

def Demo():
    global c
    c = 22
    return c

m = Demo()

print("c=",c)
print("test=", Demo())