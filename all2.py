import math
a = int(input())
b = int(input())
c = int(input())

print(a**c)
for x in range(1,c+1):
    if x == 1:
        print(c * a**(c-x) * b**(x),"x")
    else:
        print(int( (math.factorial(c)//(math.factorial(x)*math.factorial(c-x))) * a**(c-x) * b**(x)),"x ^",x)
