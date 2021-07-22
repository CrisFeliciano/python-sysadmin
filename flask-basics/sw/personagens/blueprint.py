import flask
from bson.json_util import dumps
# from sw.personagens import models
from . import models # ^^^ mesma coisa
from config.api import cabecalhos

bp = flask.Blueprint("personagens", __name__, url_prefix="/personagens")

@bp.route("")
def index():
    personagens = list(models.get_personagens())
    return flask.render_template("personagens/index.html",
                                 personagens=personagens)
    #                                  ^^^^^ variável na função
    #                            ^^^^^ variável no template

@bp.route("/<id>/editar", methods=["GET", "POST"])
def editar_personagem(id):
    if flask.request.method == 'GET':
        personagem = models.get_personagem(id)
        return flask.render_template("personagens/edit.html",
                                     personagem=personagem)

    elif flask.request.method == 'POST':
        novo_nome = flask.request.form['personagem_nome']
        models.modificar_personagens(id, {'nome': novo_nome})
        return flask.redirect(flask.url_for("personagens.index"))

@bp.route("")
def listar_personagens():
    personagens = dumps(list(models.get_personagens()))
    return flask.Response(personagens, headers=cabecalhos)

@bp.route("/criar", methods=["GET", "POST"])
def criar_personagem():
    if flask.request.method == 'GET':
        return flask.render_template("personagens/edit.html",
                                     verbo="Criar")

    elif flask.request.method == 'POST':
        nome = flask.request.form['personagem_nome']
        models.criar_personagens({'nome': nome})
        return flask.redirect(flask.url_for("personagens.index"))

@bp.route("api/<int:id>")
def get_personagem(id):
    personagem = dumps(list(models.get_personagens())[id])
    return flask.Response(personagem, headers=cabecalhos)

@bp.route("/<id>/deletar")
def deletar_personagem(id):
    models.deletar_personagem(id)
    return flask.redirect(flask.url_for("personagens.index"))

@bp.route("api/<int:id>", methods=["PUT"])
def modificar_personagem(id):
    personagem = flask.request.json
    personagens = list(models.get_personagens())
    personagem_velha = personagens[id]
    result = models.modificar_personagem(
        {"_id": personagem_velha["_id"]},
        personagem
    )
    return flask.jsonify({
        "modificados": result.modified_count
    })