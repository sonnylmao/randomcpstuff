from collections import Counter
a = input().split()
b = input().split()
ans = []
n = []
for x in b:
    n.append(len(x))

for x in a:
    if len(x) in n:
        c = 0
        for m in range(len(b)):
            if len(x) == len(b[m]):
                p = Counter(x) & Counter(b[m])
                if sum(p.values()) >= 4:
                    ans.append(b[m])
                    break
            c += 1
        if c == len(b):
            ans.append(x)
    else:
        ans.append(x)

print(*ans)
