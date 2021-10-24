import random as rnd

"""
basic genetic algorithm
"""

# population définition:
"""un individu est défini par une liste de mot binaire de type:
0110...111000 chaaque mot de la liste fait la même taille
et chaque individu de la population comporte une liste d e la même taille
taille de la liste: nb de salle
taille du mot : nb d'opérations
signification du mot:
le mot représente les opérations utiliser
la position dans la liste donne dans quel salle d'opération on parle
un 1 signifie que l'op est incluse
un 0 signifie qu'elle n'est pas incluse
"""

class individu :

    def __innit__(self):
        self.bin = []
        self.value = 0
        self.liste_salle_value= []
        self.liste_op_ban =[]
        self.liste_op_value =[]

    def set_liste_salle(self,L):
        self.liste_salle_value=L

    def set_liste_op(self,L):
        self.liste_op_value=L

    def set_bin (self):
        self.bin = [[0]*len(self.liste_op_value)]*len(self.liste_salle_value)

    def change_bin_1 (self,salle,op):
        L= self.search_in_op_ban(op)
        if L== True:
            self.bin[salle][op] = 1
            self.liste_op_ban.append(op)

    def reprogramme_op(self,op,nvalue):
        self.liste_op_value[op]=nvalue

    def reprogramme_salle(self,salle,nvalue):
        self.liste_salle_value[salle]=nvalue

    def calculate_value_room(self,salle):
        L = self.bin[salle]
        valeur = 0
        for i in range (len (L)):
            if L[i] == 1 :
                valeur += self.liste_op_value[i]
        return valeur

    def feasability(self):
        L= True
        for i in range(len(self.liste_salle_value)):
            L = L and self.calculate_value_room(i)==self.liste_salle_value[i]
        return L

    def set_value(self):
        for i in range(len(self.liste_salle_value)):
            self.value += self.calculate_value_room(i)


    def improve_feasability_(self):
        pass

    def search_in_op_ban(self,op):
        L=True
        for i in self.liste_op_ban:
            L = L and i !=op
        return L