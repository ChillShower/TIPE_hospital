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


class Individu:

    def __init__(self, salle, op):
        self.bin = [[0] * len(op)] * len(salle)
        self.value = 0
        self.liste_salle_value = salle
        self.liste_op_ban = []
        self.liste_op_value = op
        self.feasable = True

    def change_bin_1(self, salle, op):
        if self.liste_op_ban !=[]:
            L = self.search_in_op_ban(op)
        else:
            L = True
        if L:
            self.bin[salle][op] = 1
            self.liste_op_ban.append(op)

    def change_bin_0(self, salle, op):
        L = self.search_in_op_ban(op)
        if not (L):
            self.bin[salle][op] = 0
            self.liste_op_ban.remove(op)

    def reprogramme_op(self, op, nvalue):
        self.liste_op_value[op] = nvalue

    def reprogramme_salle(self, salle, nvalue):
        self.liste_salle_value[salle] = nvalue

    def calculate_value_room(self, salle):
        L = self.bin[salle]
        valeur = 0
        for i in range(len(L)):
            if L[i] == 1:
                valeur += self.liste_op_value[i]
        return valeur

    def feasability(self):
        for i in range(len(self.liste_salle_value)):
            self.feasable = self.feasable and (self.calculate_value_room(i) <= self.liste_salle_value[i])

    def set_value(self):
        for i in range(len(self.liste_salle_value)):
            self.value += self.calculate_value_room(i)

    def improve_feasability_(self):
        pass

    def search_in_op_ban(self, op):
        L = True
        for i in self.liste_op_ban:
            L = L and i != op
        return L

A=Individu([1,2,3,4,5,6,7],[1,2,3,4,5,2,8])
A.change_bin_1(2,3)