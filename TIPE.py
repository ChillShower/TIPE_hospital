class arbre :
    valeur = None
    G = None
    D = None


    def _init_ (self , valeur , aG , aD ):
        self.val = valeur
        self.G = aG
        self.D = aD

    def ajouter_fils_g (self , a ):
        self.g = a

    def ajouter_fils_d (self , a ) :
        self.d = a


Op = """liste avec temps opération croissant"""
S ="""liste avec le temps des salles"""

a = arbre(S[0])






def remplir_arbre (Op , S , a) :
    if Op == [] :
        return a
    elif :

    while S[0] != 0 :
        for i in range (len (Op)) :
            if Op[i] <= S[0] :
                a.ajouter_fils_g ("O" + str(i))
                a.ajouter_fils_d ("no" + str(i))
                S[0] = S[0] - Op[i]
            else :
                a.ajouter_fils_d ("nO" + str(i))







