"""
chaque matrice est une liste
chaque ligne de la matrice est une sous liste
"""
from random import randint as random

def aditionne(A: "matrice" , B):
    #assert A is list and B is list , "erreur: les entrées doivent être des matrices"
    assert len(A) == len(B) , "erreur: A et B ne sont pas des matrices de même dimention"
    #ASSERTIONS À COMPLÉTER
    result = []
    for y in range (len(A)):
        result.append([])
        for x in range (len(A[0])):
            result[y].append(A[y][x] + B[y][x])
    return result

def soustrait(A , B):
    #assert A is list and B is list , "erreur: les entrées doivent être des matrices"
    assert len(A) == len(B) , "erreur: A et B ne sont pas des matrices de même dimention"
    #ASSERTIONS À COMPLÉTER
    result = []
    for i in range (len(A)):
        result.append([])
        for j in range (len(A[0])):
            result[i].append(A[i][j] - B[i][j])
    return result

def multiplie(A , B):
    """
    renvoie le produit de la multiplication de la matrice A par la matrice B
    """
    assert len(A[0]) == len(B)
    result = [] # on créée la matrice résultat 
    for i in range (len(A)):
        result.append([]) # on ajoute une ligne à la matrice result afin d'y placer les résultats pour la ligne i, on répète autant de fois qu'il y a de lignes
        for jb in range (len(B[0])): # pour chaque colone j de la matrice B
            somme = 0
            for j in range (len(B)): # pour chaque ligne de la matrice B
              somme = somme + A[i][j] * B[j][jb] #on ajoute le produit de Ai,j par Bj,jb
            result[i].append(somme) # une fois qu'on a ajouté tous les produits, place ce résultat à la bonne position dans la matrice result

    return result

def est_premier(n):
    if n == 1 or n == 0 :
        return False
    for i in range (2 , n//2):
        if n % i == 0:
            return False
    return True


def gen_key():
    """
    renvoie une matrice carrée inversible d'odre 2
    """
    result = []
    for i in range(2): #génération d'une matrice aléatoire
        result.append([])# on ajoute la ligne i au résultat
        for i in range(2):
            result[-1].append(random(0,28)) # on ajoute des nombres aléatoires dans la matrice
    if det(result) == 0:
        result = gen_matrice_inv() # on recommence l'opération récursivement
    return result

def det(A: "matrice") -> float:
    """
    renvoie le déterminant d'une matrice carrée A
    """
    assert len(A) == 2 and len(A[0]) == 2 , "erreur, la matrice n'est pas une matrice carrée 2x2"
     
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0])

X = [[5 , 0 , 3],
     [0 , 7 , -2]]

Y = [[3 , 1 , -3],
     [4 , -1 , 6]]

def modulo(matrice , mod):
    for i in range (len(matrice)):
        for y in range (len(matrice[i])):
            matrice[i][y] = matrice[i][y] % mod
    return matrice

def inverse_mod(chiffre , mod):
    for i in range (1 , mod):
        if (chiffre * i) % mod == 1:
            return i
    return 0

def multiplie_int(matrice , chiffre):
    for i in range (len(matrice)):
        for j in range (len(matrice[i])):
            matrice[i][j] = matrice[i][j] * chiffre
    return matrice

def comatrice(matrice):
    matrice[0][0] , matrice[1][1] = matrice[1][1] , matrice[0][0]
    matrice[0][1] = - matrice[0][1]
    matrice[1][0] = - matrice[1][0]
    return matrice
