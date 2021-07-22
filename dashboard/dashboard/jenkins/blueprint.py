import flask as f
from flask import config
import jenkins

bp = f.Blueprint('jenkins', __name__, url_prefix='/jenkins')
client = jenkins.Jenkins(
    "http://localhost:8080",
    username="crisfeliciano", password="#Felix1988")


@bp.route("/")
def index():
    job_list = client.get_jobs()
    job_list = [client.get_job_info(j["name"])
                for j in job_list]
    return f.render_template('jenkins/index.html',
                            jobs=job_list)

@bp.route("/<name>/editar", methods=["GET", "POST"])
def edit_job(name):
    if f.request.method == "GET":
        config =  client.get_job_config(name)
        return f.render_template("jenkins/edit.html",
                                name=name, xml=config)

    xml = f.request.form["job_xml"]
    client.reconfig_job(name, xml)
    return f.redirect(f.url_for('jenkins.index'))
