import requests
def getTopicCount(topic):
    """
    La fonction getTopicCount prend en parametre 'topic' qui est un mot choisit par l'utilisteur
    et retourne le nombre d'occurence de ce mot dans l'url fournit
    """
    url = f"https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={topic}"

    response = requests.get(url)

    data = response.json()
    parse = data["parse"]
    # accede la valeur associé a parse
    text = parse["text"]
    # accede a la partie du text
    final_text = text["*"]

    count = final_text.count(topic)

    return count


topic = input("Choisir un mot : ")
print(f"Nombre d'occurences de {topic} est : ",getTopicCount(topic))
