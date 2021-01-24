a = int(input())
b = [int(d) for d in input().split()]

odd = 0
even = 0 
t = 0

for x in b:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

#e = o
if even == odd:
    t = even*2

#o > e
elif odd > even:
    if even == 0:
        if odd % 3 == 0:
            t = (odd//3)*2
        elif odd % 3 == 2:
            t = (odd//3)*2 + 1
        else:
            if (odd-4) % 3 == 0:
                t = 1 + (odd-4)//3 * 2 
    else:
        t = even*2
        if (odd-even) % 3 == 0 or (odd-even) % 3 == 1:
            t += ((odd-even)//3)*2
        else:
            t += ((odd-even)//3)*2 + 1

#o < e
else:
    t = odd*2 + 1

print(t)