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

arbre = arbre(S[0])

def remplir_arbre (Op , S):
    init( S[0] )
    for i in Op :
        if Op[i] < S[0] :
            arbre.ajouter_fils_g ("O"+str(i))
            arbre.ajouter_fils_d ("nO"+str(i))
            S[0] = S[0] - Op[i]
        else :
            arbre.ajouter_fils_d ("nO"+str(i))




def remplir_arbre_rec (Op , S , arbre) :
    if S[0] != 0 :
        arbre.ajouter_fils_d ()






