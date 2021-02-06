ans = []
bias = ['B','I','A','S']
for x in range(int(input())):
    c = 0
    a = input()
    b = [char for char in a]
    for y in b:
        if c == 4:
            
            break
        if y == bias[c]:
            c += 1
        if c == 4:
            ans.append(a)
            break

if len(ans) == 1:
    print("There is 1 biased word:")
    print(*ans,sep=", ")
elif len(ans) > 1:
    print("There are",str(len(ans)),"biased words:")
    print(*ans,sep=", ")
else:
    print("There are no biased words")