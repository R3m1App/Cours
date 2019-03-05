#coding:utf-8

"""
    Nommer une variable :   doit commencer par une lettre ou un underscore
                            ne pas contenir de caracteres speciaux
                            ne pas contenir d'espace
                            utiliser les underscores

    Type standard       :   entier numerique (int)
                            nombre flottant (float)
                            chaine de caracteres (str)
                            booleen (bool)
                            autres (listes, dictionnaire, tuples, etc....)

    Fonctions vues      :   print() -> afficher à l'écran
                            input() -> lire au clavier
                            type() -> retourne le type de donnée, variable, etc...
                            str.format() -> formater une chaine
                            int(), float(), str(), bool() -> "caster" une donnée, la convertir
"""

agePersonne = 14        #Entier
prixHT = 120.46         #Flottant
agePersonne2 = "25"     #Texte
contnuerPartie = True   #Booleen
print("-------------------------------------------")
print("agePersonne :", agePersonne, "\t| Type :", type(agePersonne))
print("prixHT :", prixHT, "\t| Type :", type(prixHT))
print("agePersonne2 :", agePersonne2, "\t| Type :", type(agePersonne2))
print("continuerPartie :", contnuerPartie, "\t| Type :", type(contnuerPartie))
print("-------------------------------------------")
texte = "L'âge de la personne est {} et le prix est de {} euros."
print(texte.format(agePersonne, prixHT))
print("-------------------------------------------")
nomJoueur = input("Saisir un nom de joueur : ")
print("Bienvenue", nomJoueur)
print("-------------------------------------------")
prixHT = float(input("Entrez un prix HT : "))
prixTTC = prixHT + (prixHT * 20 / 100)
print("Prix TTC =", prixTTC)
print("-------------------------------------------")