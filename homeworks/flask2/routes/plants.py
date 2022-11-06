from app import app
from models.models import Plant
from flask import render_template, request, redirect


@app.route("/add-plant")
def add_plant():
    return render_template("add_plant.html")


@app.route("/save-plant", methods=["POST"])
def save_plant():
    print(request.form)
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(name, location)
    plant.save()
    return redirect("/")


@app.route("/plant_info/<int:id>")
def plant_info(id):
    plant_employees = Plant.get_by_id(id)
    return render_template('plant_info.html', plant=plant_employees[0], employees=plant_employees[1])


@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    Plant.delete(id)
    return redirect("/")
