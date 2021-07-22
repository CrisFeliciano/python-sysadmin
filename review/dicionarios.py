import pprint

linux4 = {
    "cursos": [
        {"id": 521, "nome": "Python SysAdmin",
         "grupos": [
            {
                "id": 7762,
                "estudantes": [
                    "Diogo", "Thiago", ...
                ]
            }
         ]}
    ]
}

# pprint.pprint(linux4)

#for chave in linux4:
#    for curso in linux4[chave]:
#        for (chave2, valor2) in curso.items():
#            print(chave2, valor2)

#print(linux4.get("cursos", 123))
grupos = linux4["cursos"][0].pop("grupos")

#print(grupos)
#print(linux4)

linux4.update({'cursos': [], 'salas': []})
print(linux4)

linux4["nomes"] = 0
print(linux4)