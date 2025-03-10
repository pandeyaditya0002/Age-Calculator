from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    try:
        dob_str = request.form.get("dob")
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day
        
        if days < 0:
            months -= 1
            days += (today.replace(month=today.month - 1, day=1) - today.replace(day=1)).days
        if months < 0:
            years -= 1
            months += 12
        
        return jsonify({"years": years, "months": months, "days": days})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
