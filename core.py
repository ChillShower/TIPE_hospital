import indiv
import random as rdt
"""
récap de l'algo:
on génère une liste d'individu(100 disons tous neutre)
on génère un nb de couple aléatoire (de max nb op)
ces couples contienne (salle , op)
on les incorpore dans l'individu.
on répète pour chaque individu de la liste
on teste la fesabilité -> si impossible alors on améliore
on calcule la valeur de chaque individu on garde ceux qui ont la plsu élevé
on tue les autres et on effectue des mutations sur nos meilleurs (max 10% du nb d'op de mutation)
on répète un nb convenable de fois trouvé par expérience
"""
salle= []
op =[]
n = len(op)
p= len(salle)
nb_survivant=5
nb_occurence= 100
# generation 1
def generation_1():
    generation = []

    for i in range(10):
        generation.append(indiv.Individu(salle, op))
    L = []

    for ind in generation:
        for i in generate(n,p):
            ind.change_bin_1(i[0] , i[1])
        ind.feasability()
        L.append(ind.feasable)
    value =[[0,0]]*nb_survivant
    for i in range(L):
        if L[i]:
            ind_val = generation[i].set_value()
            for a in range (nb_survivant):
                if ind_val >= value[a]:
                    for k in range (1,nb_survivant-a-1):
                        value[nb_survivant -k+1] = value[nb_survivant-k]
                    value[a] = [ind_val,i]
    if value[0]==[0,0]:
        return generation_1()
    survivant = []
    for i in value:
        if i==[0,0]:
            survivant.append(generation[value[0][1]])
        else:
            survivant.append(generation[i[1]])
    return survivant

def generate(n,p):
    L=[]
    nb_couple = rdt.randint(1,n)
    for i in range(nb_couple):
        L.append([rdt.randint(0,p),rdt.randint(0,n)])
    return L

#generation k:
gen = generation_1()
liste_gen = [gen]
for i in range (nb_occurence):