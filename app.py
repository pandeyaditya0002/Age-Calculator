from flask import Flask, render_template, request, jsonify
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    try:
        birth_date_str = request.form['birthdate']
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        today = date.today()

        # Calculate difference
        age_days = (today - birth_date).days
        years = age_days // 365
        months = (age_days % 365) // 30  # Approximate month count
        days = (age_days % 365) % 30  # Remaining days

        return jsonify({"years": years, "months": months, "days": days})

    except Exception as e:
        return jsonify({"error": "Invalid Date Format"}), 400

if __name__ == "__main__":
    app.run(debug=True)
