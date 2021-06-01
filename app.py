# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Home = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
  if request.method == "POST":
    numBedRooms = request.form["numBedRooms"]
    numBathRooms = request.form["numBathRooms"]
    condition = request.form["condition"]
    houseAge = request.form['houseAge']
    houseSq = request.form["houseSq"]
    print(numBedRooms)
    print(numBathRooms)
    print(condition)
    print(houseAge)
    print(houseSq)
    #pet = Pet(name=name, lat=lat, lon=lon)
    #db.session.add(pet)
    #db.session.commit()
    #return redirect("/", code=302)
  return render_template("form.html")


if __name__ == "__main__":
    app.run()
