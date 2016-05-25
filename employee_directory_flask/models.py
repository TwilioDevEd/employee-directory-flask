from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Employee(db.Model):
    __tablename__ = 'employees'

    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, primary_key=True)
    phone_number = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
