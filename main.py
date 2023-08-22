from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("mode.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    experience = float(request.form.get("experience"))
    salary = model.predict([[experience]])
    return f"your salary will be = {salary[0]}"


app.run(host="0.0.0.0", port=4000, debug=True)
