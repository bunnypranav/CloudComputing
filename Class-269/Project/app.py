# Download the helper library from https://www.twilio.com/docs/python/install
import os
from pathlib import Path
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path("/Class-269/Project/.env"))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


# Define route and Verify_otp() function below
@app.route("/login", methods=["POST"])
def verify_otp():

    username = request.form["username"]
    password = request.form["password"]
    mobile_number = request.form["number"]

    if username == "admin" and password == "password":
        account_sid = os.environ.get("account_sid")
        auth_token = os.environ.get("auth_token")
        service_SID = os.environ.get("service_SID")
        client = Client(account_sid, auth_token)

        verification = client.verify.v2.services(service_SID).verifications.create(
            to=mobile_number, channel="sms"
        )
        print(verification.status)
        return render_template("otp_verify.html")
    else:
        return "Entered Username or Password is wrong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
