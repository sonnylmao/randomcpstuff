D = {
    3: ["happy","excited"], 
    5: "sad", 
    12: "angry", 
    9: "scared", 
    14: ["disgusted","confused"], 
    11: "surprised", 
    8: "nervous", 
    7: "deceased"
    }

x = int(input())
if len(D[x]) == 2:
    print(*D[x], sep= " or ") 
else:
    print(D[x])