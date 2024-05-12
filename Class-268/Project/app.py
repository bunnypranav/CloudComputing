import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("upload.html")


@app.route("/", methods=["POST"])
def upload_image():
    # write the code from here
    width = int(request.form["width"])
    height = int(request.form["height"])

    image_file = request.files["file"]
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join("static/", filename))
    image = Image.open(image_file)
    image.thumbnail((width, height))
    image.save(os.path.join("static/", "resized.jpg"))
    resized_image = "resized.jpg"

    return render_template("upload.html", filename=resized_image)


@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for("static", filename=filename))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
