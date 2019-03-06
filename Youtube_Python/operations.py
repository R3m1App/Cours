#coding:utf-8

"""
    Opérateurs Python :     + (addition)
                            - (soustraction)
                            * (mutlitplication)
                            / (division)
                            % (modulo) -> reste d'une division Euclidienne

    variable = variable + X
    =
    variable += X

    variable = variable - X
    =
    variable -= X

    variable = variable * X
    =
    variable *= X

    variable = variable / X
    =
    variable /= X
"""

print("------------------------------------")

calcul = 5 / 2
calculInt = int(calcul)
calculFloat = float(calcul)

calcul2 = 5 % 2

print("Résultat(int) =\t\t", calculInt)
print("Résultat(float) =\t", calculFloat)
print("Modulo Calcul2 = \t", calcul2)

print("------------------------------------")

niveauPersonnage = int(input("Niveau de départ ?"))
print("Niveau Personnage :", niveauPersonnage)
print("Victoire!!!! Tu gagnes deux niveaux.")
niveauPersonnage += 2
print("Niveau Personnage :", niveauPersonnage)