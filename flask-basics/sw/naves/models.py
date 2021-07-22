from bson.objectid import ObjectId
from config.db import db

def get_naves():
    return db.naves.find()

def get_nave(oid):
    filtro = {"_id": ObjectId(oid)}
    return db.naves.find_one(filtro)

def criar_nave(nave):
    return db.naves.insert_one(nave)

def modificar_nave(oid, nave):
    if isinstance(oid, str):
        oid = {"_id": ObjectId(oid)}

    return db.naves.update_one(
        oid,
        {"$set": nave}
    )

def deletar_nave(oid):
    if isinstance(oid, str):
        oid = {"_id": ObjectId(oid)}

    return db.naves.delete_one(oid)
