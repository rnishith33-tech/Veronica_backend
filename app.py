from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # ✅ allows your Netlify website to talk to backend

# Home route (test)
@app.route("/")
def home():
    return "Veronica is running!"

# Command route
@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    text = data.get("text", "").lower()

    # Basic commands
    if "veronica" in text:
        reply = "Yes, I am here. How can I help you?"
    
    elif "time" in text:
        reply = "The time is " + datetime.datetime.now().strftime("%H:%M")
    
    elif "date" in text:
        reply = "Today is " + datetime.datetime.now().strftime("%d %B %Y")
    
    elif "hello" in text:
        reply = "Hello! How can I assist you?"
    
    else:
        reply = "Sorry, I did not understand that."

    return jsonify({"reply": reply})

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
