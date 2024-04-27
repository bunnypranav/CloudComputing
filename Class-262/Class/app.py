# import flask library along with flask render template, request and requests
from flask import Flask, render_template, request
import requests

# initialize flask
app = Flask(__name__)


# Define visitor function to check how many visitor are there
@app.route("/")
def visitors():

    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    visitors_count += 1

    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable
    return render_template("index.html", count=visitors_count)


# Add route for your webpage


@app.route("/", methods=["POST"])
def weather_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    # Get latitude and longitude from the from
    lat = request.form["lat"]
    long = request.form["long"]

    # Call the weather api 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude and return weather and visitor count while rendering index.html
    response = requests.get(
        f"https://weather-l6tl.onrender.com/api/getCurrentWeather/{lat}/{long}"
    )
    data = response.json()
    print(data)
    return render_template("index.html", weather=data, count=visitors_count)


# add code for executing flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
