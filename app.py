import os
from flask import Flask, render_template, request

app = Flask(__name__)

TEXT_FILE = "data/text_data.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(TEXT_FILE), exist_ok=True)

    if request.method == "POST":
        # Save updated text
        new_text = request.form["editable_text"]
        with open(TEXT_FILE, "w") as f:
            f.write(new_text)

    # Read current text or create the file with default content if missing
    if not os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "w") as f:
            f.write("Default text")

    with open(TEXT_FILE, "r") as f:
        current_text = f.read()

    return render_template("index.html", text=current_text)

@app.route("/scan", methods=["GET"])
def scan():
    # Read current text and return as plain text
    if not os.path.exists(TEXT_FILE):
        return "No text available"
    with open(TEXT_FILE, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)