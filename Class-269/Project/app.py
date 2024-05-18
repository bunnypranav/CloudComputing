from flask import Flask, render_template, request, redirect, url_for, send_file
from twilio.rest import Client
import os

app = Flask(__name__)


@app.route("/")
def loadHTML():
    print("HTML Loaded")
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
