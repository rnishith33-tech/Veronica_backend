# =========================================================
# app.py
# VERONICA BACKEND (CHAT + ECG DASHBOARD)
# =========================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from voicewithbrain import process_command
import datetime

app = Flask(__name__)
CORS(app)  # ✅ allow frontend (Netlify) to connect

# =========================================================
# TEMP STORAGE FOR ECG DATA
# =========================================================

ecg_data = []

# =========================================================
# HOME ROUTE
# =========================================================

@app.route("/")
def home():
    return "Veronica is running!"

# =========================================================
# CHATBOT ROUTE (VERONICA BRAIN)
# =========================================================

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_text = data.get("text", "")

        reply = process_command(user_text)

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

# =========================================================
# RECEIVE ECG DATA FROM ESP32
# =========================================================

@app.route("/ecg", methods=["POST"])
def receive_ecg():
    try:
        data = request.get_json()
        value = data.get("value")

        ecg_data.append({
            "value": value,
            "time": datetime.datetime.now().strftime("%H:%M:%S")
        })

        # Keep only last 100 values
        if len(ecg_data) > 100:
            ecg_data.pop(0)

        return jsonify({"status": "received"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# =========================================================
# SEND ECG DATA TO WEBSITE
# =========================================================

@app.route("/get-ecg", methods=["GET"])
def get_ecg():
    return jsonify(ecg_data)

# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
