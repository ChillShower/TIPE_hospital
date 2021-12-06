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
salle = [1, 2, 3]
op = [5, 1, 2, 3, 2, 1]
n = len(op)
p = len(salle)
nb_survivant = 3
taille_generation = 100
nb_occurence = 1000


# generation 1

def generation_1():
    generation = []

    for i in range(taille_generation):  # genere tout les individus
        generation.append(indiv.Individu(salle, op))
    L = []

    for ind in generation:  # set les values aléatoires + la lsite  de feasabilité
        for i in generate(n, p):
            ind.change_bin_1(i[0], i[1])
        ind.feasability()
        L.append(ind.feasable)
    value = [[0, 0] for i in range(nb_survivant)]
    for i in range(len(L)):  # parcours les individu utiliseable
        if L[i]:
            generation[i].set_value()
            ind_val = generation[i].value
            a = nb_survivant - 1
            if ind_val >= value[a][0]:
                value[a] = [ind_val, i]
                a -= 1
                while a >= 0 and ind_val > value[a][0]:
                    value[a + 1] = value[a]
                    value[a] = [ind_val, i]
                    a -= 1

    survivant = []
    for i in value:
        if i == [0, 0]:
            survivant.append(generation[value[0][1]])
        else:
            survivant.append(generation[i[1]])
    return survivant


def generate(n, p):  # genere les liste a remplacer
    L = []
    nb_couple = rdt.randint(1, n)
    for i in range(nb_couple):
        L.append([rdt.randint(0, p - 1), rdt.randint(0, n - 1)])
    return L


# generation k:
def select(L):
    list = [[0, 0] for i in range(nb_survivant)]
    for i in range(len(L)):
        a = nb_survivant - 1
        ind = L[i]
        ind.set_value()
        valu = ind.value
        if valu > list[a][0]:
            list[a] = [valu, i]
            a -= 1
            while a >= 0 and valu > list[a][0]:
                list[a + 1] = list[a]
                list[a] = [valu, i]
                a -= 1
    ret_liste = []
    for i in list:
        ret_liste.append(L[i[1]])
    return ret_liste


def naissance(gen):
    individu = indiv.Individu(salle, op)
    pere = rdt.randint(0, nb_survivant - 1)
    mere = rdt.randint(0, nb_survivant - 1)
    while pere == mere:
        mere = rdt.randint(0, nb_survivant - 1)
    for i in range(p):
        for t in range(n):
            genom = rdt.random()
            if genom > 0.5:
                a = gen[pere].bin[i][t]
                if a == 1:
                    individu.change_bin_1(i, t)
            else:
                a = gen[mere].bin[i][t]
                if a == 1:
                    individu.change_bin_1(i, t)
    return individu


def reproduction(gen):
    new_gen = []
    for i in range(taille_generation):
        indiv = naissance(gen)
        indiv.feasability()
        if indiv.feasable:
            new_gen.append(indiv)
    return new_gen


def mutation(gen):
    new_gen = []
    for ind in gen:
        a = generate(n, p)
        for elt in a:
            b = rdt.random()
            if b > (1 / 2):
                ind.change_bin_0(elt[0], elt[1])
            else:
                ind.change_bin_1(elt[0], elt[1])
        ind.feasability()
        if ind.feasable:
            new_gen.append(ind)
    return new_gen


def next_gen(gen):  # but changer un peu les solutions et ne garder que les feasable
    l_individu = gen
    new_gen = reproduction(gen)
    gen_finale = mutation(new_gen)
    return l_individu + gen_finale


gen = generation_1()
l_gen = [gen]
for i in range (nb_occurence):
    gen = next_gen(gen)
    gen = select(gen)
    l_gen.append(gen)








