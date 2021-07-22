import docker
import flask
import sw.naves.blueprint as naves
import sw.personagens.blueprint as personagens
from config.db import setup

app = flask.Flask(__name__)  # dois underlines
app.register_blueprint(naves.bp)
app.register_blueprint(personagens.bp)
@app.route("/")
def home():
    return 'home'

# @app.route("/personagens")
# def listar_personagens():
#     return flask.jsonify(sw.personagens)

if __name__ == "__main__":  # também com 2 underlines
    docker.DockerClient().containers.get('mongo-sw').start()
    setup()
    app.run(debug=True)
