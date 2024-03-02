def entryTime(s, keypad):
    """
        entryTime calcule le temps pour taper le code "s" sur le clavier "keypad"
    """
    pos = {}
    # Création d'un dictionnaire pour mapper chaque chiffre du clavier à sa position
    for i in range(len(keypad)):
        pos[keypad[i]] = (i // 3, i % 3)
    temps = 0
    curPos = pos[s[0]]
    for i in range(1, len(s)):
        nextPos = pos[s[i]]
        #Calcul du temps de déplacement entre la position courante et la prochaine position
        #en prenant le maximum entre la différence absolue des lignes et des colonnes
        distance = max(abs(nextPos[0] - curPos[0]), abs(nextPos[1] - curPos[1]))
        temps += distance
        curPos = nextPos
    return temps


while True:
    s = input("Entrez le code : ")
    #Le code doit contenir que des chiffres
    if s.isdigit():
        break
    else:
        print("Le code doit contenir que des chiffres ! ")
while True:
    keypad = input("Entrez le keypad : ")
    #keypad doit contenir 9 chiffres differents
    if len(set(keypad)) == 9 and keypad.isdigit():
        break
    else:
        print("Le keypad doit contenir 9 chiffres differents ! ")
time = entryTime(s, keypad)
print("Temps pour taper le code = ", time)
