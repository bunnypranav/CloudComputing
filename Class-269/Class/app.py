import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

load_dotenv(dotenv_path=Path("/Class-269/Class/.env"))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/token")
def generate_token():
    fake = Faker()
    username = request.args.get("username", fake.user_name())

    account_sid = os.environ.get("account_sid")
    api_key = os.environ.get("api_key")
    api_secret = os.environ.get("api_secret")
    service_SID = os.environ.get("service_SID")

    token = AccessToken(account_sid, api_key, api_secret, identity=username)
    sync_grant_access = SyncGrant(service_sid=service_SID)
    token.add_grant(sync_grant_access)

    return jsonify(identity=username, token=token.to_jwt().decode())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
