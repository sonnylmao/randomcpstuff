  
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

userchoice = input()
keyword = [char for char in input().lower()]
shift = int(input())
answer = []

if userchoice == 'ENCODE':
    for x in range(len(keyword)):
        if keyword[x] == ' ':
            answer.append(' ')
            continue
        pos = letters.index(keyword[x])
        newpos = (pos + shift) % 26
        answer.append(letters[newpos].upper())
elif userchoice == 'DECODE':
    for x in range(len(keyword)):
        if keyword[x] == ' ':
            answer.append(' ')
            continue
        pos = letters.index(keyword[x])
        newpos = (pos - shift) % 26
        answer.append(letters[newpos].upper())

print(*answer,sep='')