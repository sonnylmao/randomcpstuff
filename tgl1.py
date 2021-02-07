a = [int(d) for d in input().split()]
n = int(input())-1

for x in range(3):
    if n >= 20:
        break
    print(a[n])
    n += 1