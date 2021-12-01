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

def salle2(L):
    M=[]
    for i in range(len(2**n)):
        for j in range(len(n)):
            if L[j]==1:
                L[j]=0
                M=M+[L[j]]
            else:
                L[j]=0 or L[j]=1
                M=M+[L[j]]







"""def mot_bis(p,n):
    pass
    L=[]
    for p in range(n):
        m=mot(n-p)
        for i in range (len(m)):"""






print(mot(10))


