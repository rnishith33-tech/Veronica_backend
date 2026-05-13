from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Veronica is running!"

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    text = data.get("text", "").lower()

    if "veronica" in text:
        reply = "Yes, I am here"
    elif "time" in text:
        import datetime
        reply = datetime.datetime.now().strftime("%H:%M")
    else:
        reply = "I did not understand"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()