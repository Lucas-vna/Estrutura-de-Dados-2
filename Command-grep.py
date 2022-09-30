import re

Arq1 = open("games.txt", "r")

busca = "Final" #qualquer palavra que queria buscar

for word in Arq1:
    if re.search(busca, word):
        print(word)
