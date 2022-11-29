from app import app
from flask import render_template
from models.models import Plant, Employee


@app.route("/")
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    # plants = Plant.query.filter(Plant.location == "Peremogy Str.")
    # plants = Plant.query.order_by(Plant.id.asc()).all()
    print(plants)
    return render_template("index.html", plants=plants, employees=employees)
