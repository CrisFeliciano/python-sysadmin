
estudantes = [
    "Diogo",
    "Mario",
    "Tiago",
    "Thiago",
    "Francisco",
    "Elder",
    "Christiano",
    "Damião"
]


#print(estudantes)

#for nome in estudantes:
#    print(nome)

# print(estudantes.index('Mario'))
#print(estudantes[1])

#indice = estudantes.index("Mario")
#print(estudantes[indice])

#print(estudantes[estudantes.index("Mario")])

estudantes.append("Marcos")
print(estudantes)

estudantes.pop()
print(estudantes)

indice = estudantes.index("Francisco")
removido = estudantes.pop(indice)
print(estudantes)
print(removido)

estudantes.remove('Diogo')
print(estudantes)

estudantes.clear()
print(estudantes)

estudantes.append(None)
estudantes[0] = "Otávio"
print(estudantes)