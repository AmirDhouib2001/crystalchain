def Max_Diff(array):
    """
    La fonction prend en parametre un tableau et renvoie la difference maximal entre deux valeurs
    du tableau sous condition que la petite valeur precede la grande valeur
    """
    MaxDiff = 0
    Minimum = array[0]
    for i in range(1,len(array)):
        MaxDiff = max(MaxDiff, array[i] - Minimum)
        # Mise a jour de la difference maximale si on trouve un element plus grand que le minimum actuel
        Minimum = min(Minimum, array[i])
        # Mise a jour du minimum trouve jusqu'a maintenant

    return MaxDiff


taille = int(input("Taille du tableau : "))
array = []
for i in range(taille):
    nbr = int(input(f"Ecrit l'élement {i+1}: "))
    array.append(nbr)

maxdiff = Max_Diff(array)
print("Difference Maximal = ", maxdiff)