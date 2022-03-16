
class Arbre:
    """ Implémentation des Arbres binaires ( D = droite; G = gauche)"""

    val = None	#valeur du noeud
    fils = []		#sous arbre Gauche
    path = [] #chemin couple des listes

    def __init__(self, valeur, fils, path):
        self.val = valeur
        self.fils = fils
        self.path = path

    def ajouterFils(self, enfant):
        self.fils.append(enfant)

    def set_path(self,path):
        self.path=path



Salle = [2,5,4,3,8,6,10,6,20,1,3]
O = [3,2,2,5,4,5,3,7,2,1]
B=Arbre(0,[],[])
A= Arbre(0,[],[])
A.ajouterFils(B)




def construit_arbre (salle , op, t, path) :
    A = Arbre(t,[],[])
    A.set_path(path)
    S = salle.copy()
    if op != [] :
        for i in range(len(salle)) :
            if salle[i] >= op[0] :#opération rentre
                a=t
                S[i] -= op[0]
                p= path.copy()
                p.append(i)
                A.ajouterFils(construit_arbre(S , op[1:] ,(a+op[0]), p))
        p=path.copy()
        p.append("vide")
        A.ajouterFils(construit_arbre(S, op[1:] , t , p))
    return(A)


A=construit_arbre(Salle,O,0,[])


"""def print_arbre(a) :
    print("(", end="")
    print(a.val,end="")
    print("[",end="")
    for elt in a.fils :
        print_arbre(elt)
        print(",")
    print("]",end="")
    print(")",end="")

print_arbre(A)"""




def best (A , m , path_m) :
    fils = A.fils
    l = [] 
    if fils == [] : 
        if m > A.val : 
            return (m,path_m)
        else :
            return(A.val,A.path)
    else : 
        for i in fils : 
            l.append(best(i, m, path_m))
    L = [l[j][0] for j in range (len(l))]
    M = max (L)
    indice = L.index(M)
    return(M , l[indice][1])
    
    
print(best (A,0,[]))


