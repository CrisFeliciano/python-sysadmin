import pymongo

cliente = pymongo.MongoClient()
db = cliente.sw

def setup():
    naves = [
        {"nome": "X-Wing"},
        {"nome": "Y-Wing"}
    ]

    personagens = [
        {"nome": "Lucas Andarilho dos Céus"},
        {"nome": "Léia dos Órgãos"}
    ]

    if db.naves.count() > 0:
        return
    
    db.naves.insert_many(naves)
    db.personagens.insert_many(personagens)