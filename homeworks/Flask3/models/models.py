from app import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    plant_id = db.Column(db.Integer, nullable=False)
    type_of_work = db.Column(db.String(255), nullable=False)