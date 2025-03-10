from flask import Flask, render_template, request, jsonify
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    try:
        birthdate_str = request.form.get("birthdate")
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        today = date.today()

        # Calculate age (years, months, days)
        years = today.year - birthdate.year
        months = today.month - birthdate.month
        days = today.day - birthdate.day

        # Adjust for negative months/days
        if days < 0:
            months -= 1
            days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days
        if months < 0:
            years -= 1
            months += 12

        return jsonify({
            "years": years,
            "months": months,
            "days": days
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
