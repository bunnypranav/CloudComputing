# import flask library along with flask render template, request and requests
from flask import Flask, render_template, request
import requests

# initialize flask
app = Flask(__name__)


# Define visitor function to check how many visitor are there
@app.route("/")
def main():
    return render_template("index.html")


# Add route for your webpage


@app.route("/", methods=["POST"])
def math_operations():

    # Get latitude and longitude from the from
    eq = request.form["eq"]
    op = request.form["op"]

    # Call the weather api 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude and return weather and visitor count while rendering index.html
    response = requests.get(f"https://newton.vercel.app/api/v2/{op}/{eq}").json()
    print(response)
    return render_template(
        "index.html", r=response["result"], eq=response["expression"]
    )


# add code for executing flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
