from flask import Flask, render_template, jsonify
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, root_path=dir_path)

@app.route("/")
def home():
    return render_template("index_lf.html")

@app.route("/worldmap")
def worldmap():
    return render_template("index_worldmap.html")

@app.route("/citymap")
def citymap():
    return render_template("citymap.html")

@app.route("/calc")
def calc():
    return render_template("calc.html")

@app.route("/LE")
def life_expectancy():
    return render_template("Life_Expectancy_Index.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
