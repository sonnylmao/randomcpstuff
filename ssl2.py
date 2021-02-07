l = ['A','B','C','D','E']
a = [char for char in input()]
n1 = l.index(a[0])
while True:
    b = [char for char in input()]
    if a == b:
        print("Found")
        break
    n = l.index(b[0])
    if n1 == 4:
        if b[0] == 'D':
            if int(b[1]) == int(a[1]) or int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")
        elif b[0] == 'E':
            if int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")
        else:
            print("No Signal")
    elif n1 == 0:
        if b[0] == 'B':
            if int(b[1]) == int(a[1]) or int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")
        elif b[0] == 'A':
            if int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")
        else:
            print("No Signal")
    else:
        if b[0] == a[0]:
            if int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")
        
        elif b[0] == l[n1+1]:
            if int(b[1]) == int(a[1]) or int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")
        
        elif b[0] == l[n1-1]:
            if int(b[1]) == int(a[1]) or int(b[1]) == int(a[1]) + 1 or int(b[1]) == int(a[1]) - 1:
                print("Close Signal")
            else:
                print("No Signal")  
          
        else:
            print("No Signal")
