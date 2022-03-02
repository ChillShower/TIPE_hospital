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



S = [2,5]
O = [3,2]
B=Arbre(0,[],[])
A= Arbre(0,[],[])
A.ajouterFils(B)

##
def rec_test(n):
    a=n
    for i in range( n):
        a += rec_test(i)
    return a

print(rec_test(4))

##
def construit_arbre (salle , op, t, path) :
    A = Arbre(t,[],[])
    A.set_path(path)
    if op != [] :
        for i in range(len(salle)) :
            print(i)
            if salle[i] >= op[0] :#opération rentre
                a=t
                S = salle.copy()
                S[i] -= op[0]
                p= path.copy()
                p.append(i)
                print(p)
                A.ajouterFils(construit_arbre(S , op[1:] ,(a+op[0]), p))
        p=path.copy()
        p.append("vide")
        A.ajouterFils(construit_arbre(S, op[1:] , t , p))
    return(A)


A=construit_arbre(S,O,0,[])


def print_arbre(a) :
    print("(", end="")
    print(a.val,end="")
    print("[",end="")
    for elt in a.fils :
        print_arbre(elt)
        print(",")
    print("]",end="")
    print(")",end="")

print_arbre(A)




