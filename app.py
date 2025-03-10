from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    try:
        data = request.get_json()
        dob_str = data.get("dob")
        if not dob_str:
            return jsonify({"error": "Date of birth is required"}), 400

        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        return jsonify({"age": age})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
