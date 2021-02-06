import math

a = [int(d) for d in input().split()]

print(int(a[0]*(math.cos(a[1]*(math.pi/180))+math.sin(a[1]*(math.pi/180)))))