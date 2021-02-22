from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from employee_directory_flask.config import config_env_files

db = SQLAlchemy()

app = Flask(__name__)
Bootstrap(app)
env = app.config.get("ENV", "production")


def prepare_app(environment=env, p_db=db):
    app.config.from_object(config_env_files[environment])
    p_db.init_app(app)
    from . import views  # noqa F401

    return app
