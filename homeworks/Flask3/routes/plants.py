from app import app, db
from flask import render_template, request, redirect
from models.models import Plant


@app.route("/add-plant")
def add_plant():
    return render_template("add_plant.html")


@app.route("/save-plant", methods=["POST"])
def save_plant():
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(title=name, location=location)
    db.session.add(plant)
    db.session.commit()
    return redirect("/")


@app.route("/plant_info/<int:id>")
def plant_info(id):
    plant = Plant.query.get(id)
    print(plant.id)
    # title = request.form.get("title")
    # location = request.form.get("location")
    # plant = Plant(title=title, location=location)
    # db.session.commit()
    # plant_employees = Plant.get_by_id(id)
    return render_template('plant_info.html', title=plant.title, location=plant.location)


@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    plant = Plant.query.get(id)
    print(plant.id)
    db.session.delete(plant)
    db.session.commit()
    return redirect("/")
