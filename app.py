from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.iot_system
devices_collection = db.Devices


@app.route("/")
def home():
    devices=list(devices_collection.find())
    return render_template("home.html", devices=devices)

@app.route("/add_device", methods=["GET", "POST"])
def add_device():
    if request.method == "POST":
        device_name = request.form.get("device_name")
        if device_name:
            new_device={'name':device_name,'status':'online'}
            devices_collection.insert_one(new_device)
        return redirect(url_for("home"))
    return render_template("add_device.html")

if __name__ == "__main__":
    app.run(debug=True)
