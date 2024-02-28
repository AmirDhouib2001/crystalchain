def maxmin(array):
    MaxDiff = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            MaxDiff = max(MaxDiff, array[j] - array[i])
    return MaxDiff


taille = int(input("Taille du tab : "))
array = []
for i in range(taille):
    nbr = int(input(": "))
    array.append(nbr)

maxdiff = maxmin(array)
print("Max = ", maxdiff)