import requests

ENDPOINT_BASE = 'https://swapi.dev/api/'

ENDPOINT_PERSONAGENS = ENDPOINT_BASE + 'people'
ENDPOINT_NAVES = ENDPOINT_BASE + 'starships'

#response = requests.get(ENDPOINT_PERSONAGENS)
#dados = response.json()

#print(dados["next"])

def listar_todos_personagens_humanos():
    url_pagina = ENDPOINT_PERSONAGENS

    while url_pagina is not None:
        response = requests.get(url_pagina)
        dados = response.json()

        for personagem in dados['results']:
            if personagem['species'] == []:
                print(personagem['name'])

        url_pagina = dados['next']


def listar_naves_preco_abaixo_de(preco):
    url_pagina = ENDPOINT_NAVES

    while url_pagina is not None:
        response = requests.get(url_pagina)
        dados = response.json()

        for nave in dados['results']:
            custo = nave['cost_in_credits']
            if custo != 'unknown' and float(custo) < preco:
                print(nave['name'])

        url_pagina = dados['next']


listar_naves_preco_abaixo_de(10_000_000)
