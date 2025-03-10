from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    data = request.get_json()
    dob_str = data.get("dob")  # Get date from request

    if not dob_str:
        return jsonify({"error": "Invalid date"}), 400

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        print(f"Calculated Age: {age}")  # Debugging line
        return jsonify({"age": age})  # Return JSON response

    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400


if __name__ == "__main__":
    app.run(debug=True)
