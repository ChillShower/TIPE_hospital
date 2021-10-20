def mot(n):
    L=[]
    if n==1:
        return ["0","1"]
    else:
        m=mot(n-1)
        for i in range(len(m)):
            L.append("1"+m[i])
            L.append("0"+m[i])
        return L

def mot_bis(p,n):
    L=[]
    for p in range(n):
        m=mot(n-p)
        for i in range (len(m)):






print(mot (3))


