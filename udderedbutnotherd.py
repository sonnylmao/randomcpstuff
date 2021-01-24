import math
a = [char for char in input()]
b = [char for char in input()]

c = 0
t = 0

while c != len(b):
    for x in a:
        if c == len(b):
            break
        if x == b[c]:
            c += 1
        t += 1

print(math.ceil(t/26))

