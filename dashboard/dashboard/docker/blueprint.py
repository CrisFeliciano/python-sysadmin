import flask as f
import docker

bp = f.Blueprint("docker", __name__, url_prefix="/docker")
client = docker.DockerClient()

@bp.route("")
def index():
    cs = client.containers.list(all=True)
    return f.render_template(
        "docker/index.html",
        containers=cs)

@bp.route("/<id>/executar")
def start_container(id):
    client.containers.get(id).start()
    return f.redirect(f.url_for('docker.index'))

@bp.route("/<id>/parar")
def stop_container(id):
    client.containers.get(id).stop()
    return f.redirect(f.url_for('docker.index'))

@bp.route("/<id>/remover")
def remove_container(id):
    client.containers.get(id).remove()
    return f.redirect(f.url_for('docker.index'))