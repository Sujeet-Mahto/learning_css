from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/packages")
def packages():
    return render_template("packages.html")


if __name__ == "__main__":
    app.run(debug=True)
