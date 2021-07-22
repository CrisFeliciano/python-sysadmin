import flask
from bson.json_util import dumps
# from sw.naves import models
from . import models # ^^^ mesma coisa
from config.api import cabecalhos

bp = flask.Blueprint("naves", __name__, url_prefix="/naves")

#### Web ####

@bp.route("")
def index():
    naves = list(models.get_naves())
    return flask.render_template("naves/index.html",
                                 naves=naves)
    #                                  ^^^^^ variável na função
    #                            ^^^^^ variável no template

@bp.route("/<id>/editar", methods=["GET", "POST"])
def editar_nave(id):
    if flask.request.method == 'GET':
        nave = models.get_nave(id)
        return flask.render_template("naves/edit.html",
                                     verbo="Editar",
                                     nave=nave)

    elif flask.request.method == 'POST':
        novo_nome = flask.request.form['nave_nome']
        models.modificar_nave(id, {'nome': novo_nome})
        return flask.redirect(flask.url_for("naves.index"))

@bp.route("/criar", methods=["GET", "POST"])
def criar_nave():
    if flask.request.method == 'GET':
        return flask.render_template("naves/edit.html",
                                     verbo="Criar")

    elif flask.request.method == 'POST':
        nome = flask.request.form['nave_nome']
        models.criar_nave({'nome': nome})
        return flask.redirect(flask.url_for("naves.index"))

@bp.route("/<id>/deletar")
def deletar_nave(id):
    models.deletar_nave(id)
    return flask.redirect(flask.url_for("naves.index"))

#### API ####

@bp.route("api")
def listar_naves():
    naves = dumps(list(models.get_naves()))
    return flask.Response(naves, headers=cabecalhos)

@bp.route("api", methods=["POST"])
def criar_nave_api():
    nave = flask.request.json
    result = models.criar_nave(nave)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("api/<int:id>")
def get_nave(id):
    nave = dumps(list(models.get_naves())[id])
    return flask.Response(nave, headers=cabecalhos)

@bp.route("api/<int:id>", methods=["PUT"])
def modificar_nave(id):
    nave = flask.request.json
    naves = list(models.get_naves())
    nave_velha = naves[id]
    result = models.modificar_nave(
        {"_id": nave_velha["_id"]},
        nave
    )
    return flask.jsonify({
        "modificados": result.modified_count
    })