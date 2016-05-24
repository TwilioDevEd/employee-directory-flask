from employee_directory_flask.config import config_env_files
from employee_directory_flask.models import db
from flask import Flask

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


def prepare_app(environment='development', p_db=db):
    app.config.from_object(config_env_files[environment])
    p_db.init_app(app)
    from . import views
    return app


def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
db.save = save_and_commit
