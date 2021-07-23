from typing import Container
import flask as f
import docker

bp = f.Blueprint("docker", __name__, url_prefix="/docker")
client = docker.DockerClient()

@bp.route("")
def index():
    print(f.current_app.logger.level)
    f.current_app.logger.info("listando conteiner do docker")
    cs = client.containers.list(all=True)
    return f.render_template(
        "docker/index.html",
        containers=cs)

@bp.route("/<id>/executar")
def start_container(id):
    container = client.containers.get(id)
    f.current_app.logger.info(f"startando {id}")
    client.containers.get(id).start()
    container.start()
    f.flash(f"{container.name} startado", "info")
    return f.redirect(f.url_for('docker.index'))

@bp.route("/<id>/parar")
def stop_container(id):
    container = client.containers.get(id)
    f.current_app.logger.info(f"parando {id}")
    client.containers.get(id).stop()
    container.stop()
    f.flash("{id} stopado", "warn")
    return f.redirect(f.url_for('docker.index'))

@bp.route("/<id>/remover")
def remove_container(id):
    f.current_app.logger.info(f"removendo {id}")
    client.containers.get(id).remove()
    return f.redirect(f.url_for('docker.index'))