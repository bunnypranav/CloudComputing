import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("upload.html")


@app.route("/", methods=["POST"])
def upload_image():
    operation_selection = request.form["image_type_selection"]
    image_file = request.files["file"]
    filename = secure_filename(image_file.filename)
    reading_file_data = image_file.read()
    image_array = np.fromstring(reading_file_data, dtype="uint8")
    decode_array_to_img = cv2.imdecode(image_array, cv2.IMREAD_UNCHANGED)

    # Write code for Select option for Gray and Sketch
    if operation_selection == "gray":
        file_data = make_grayscale(decode_array_to_img)
    elif operation_selection == "sketch":
        file_data = image_sketch(decode_array_to_img)
    else:
        print("No image type selected")

    # Ends here

    with open(os.path.join("static/", filename), "wb") as f:
        f.write(file_data)

    return render_template("upload.html", filename=filename)


def make_grayscale(decode_array_to_img):

    converted_gray_img = cv2.cvtColor(decode_array_to_img, cv2.COLOR_RGB2GRAY)
    status, output_image = cv2.imencode(".PNG", converted_gray_img)

    return output_image


# Write code for Sketch function
def image_sketch(decode_array_to_img):
    convertedImg = cv2.cvtColor(convertedImg, cv2.COLOR_BGR2GRAY)
    sharpingImg = cv2.bitwise_not(decode_array_to_img)
    blurImg = cv2.GaussianBlur(sharpingImg, (111, 111), 0)
    sharpingBlurImg = cv2.bitwise_not(blurImg)
    sketchImg = cv2.divide(convertedImg, sharpingBlurImg, scale=256.0)
    status, output = cv2.imencode(".PNG", sketchImg)
    return output


# Ends here


@app.route("/display/<filename>")
def display_image(filename):

    return redirect(url_for("static", filename=filename))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
