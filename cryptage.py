from calcul_matriciel import *


char = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , ' ' , '?' , '!']

number = {}
for i in range (len(char)):
    number[char[i]] = i
print(number)

def recup_texte():
    print("entrez votre message")
    text = input("appuyez sur entrée une fois terminé     ")
    text = text + " " * (len(text) % 2 == 1) #opération booléenne plus rapide qu'un if, ajoute un " " à la fin du message si le nombre de caractères est impair
    return text

def transforme_texte(text):
    """
    renvoie les matrices des numéros des caractères
    """
    text_pile = list(text)
    tab = []
    for i in range (len(texte) >> 1): # on parcourt le texte (sa longueur/2)fois car on crée des groupes(matrices) de 2 caractères (>>1) est un décalage de bit permetant de diviser par 2 sans faire de division (plus rapide)
        tab.append([]) #on ajoute une matrice (un groupe) au tableau
        for i in range(2):
            tab[-1].append([])#on ajoute une ligne au groupe
            tab[-1][-1].append(number[text_pile.pop()])#on place le numéro caractère à la fin de la pile dans la ligne
    return tab

def transforme_matrice(tab):
    """
    renvoie le message texteassocié à la matrice des groupes de caractères
    """
    texte = str()
    while len(tab) != 0: # tant qu'il y a encore des matrices dans le tableau
        matrice = tab.pop() # on retire la matrice du haut de la pile
        for i in range(len(matrice)): # pour chaque ligne/numéro de la matrice 
            texte = texte + char[matrice.pop()[0]] #on ajoute le caractère associé au numéro au texte
    return texte

def cryptage (message: list , key : list):
    msg = transforme_texte(message[::-1])
    for i in range (len(msg)):
        msg[i] = multiplie(key , msg[i])
    for i in range(len(msg)):
        msg[i] = modulo(msg[i] , 29)
    msgtxt = transforme_matrice(msg)
    return msgtxt[::-1]

def decryptage (message , key):
    msg = transforme_texte(message[::-1])
    determinant = det(key)
    dkey = comatrice(key)
    dkey = multiplie_int(dkey , inverse_mod(determinant , 29))
    dkey = modulo(dkey , 29)
    for i in range (len(msg)):
        msg[i] = multiplie(dkey , msg[i])
    for i in range (len(msg)):
        msg[i] = modulo(msg[i] , 29)
    msgtxt = transforme_matrice(msg)
    return msgtxt[::-1]

texte = recup_texte()
print("voici votre message : " , texte)
key = gen_key()
print("voici la cle" , key)
cypher = cryptage(texte , key)
print("voici le message crypte:" , cypher)
decrypt = decryptage(cypher , key)
print("en decryptant le message" , decrypt)

