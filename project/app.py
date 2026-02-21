from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 🔴 backend validation
        for key, value in request.form.items():
            if value.strip() == "":
                return render_template("index.html", error="Please fill all fields")

        MinTemp = float(request.form['MinTemp'])
        MaxTemp = float(request.form['MaxTemp'])
        Rainfall = float(request.form['Rainfall'])
        Humidity9am = float(request.form['Humidity9am'])
        Humidity3pm = float(request.form['Humidity3pm'])
        Pressure9am = float(request.form['Pressure9am'])
        Pressure3pm = float(request.form['Pressure3pm'])

        # ⭐ rule based prediction
        if (Humidity3pm > 70 and Pressure3pm < 1010) or Rainfall > 0:
            return render_template("chance.html")
        else:
            return render_template("noChance.html")

    except:
        return render_template("index.html", error="Invalid numeric input")

if __name__ == "__main__":
    app.run(debug=True)
