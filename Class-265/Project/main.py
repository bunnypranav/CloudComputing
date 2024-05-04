import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("upload.html")


@app.route("/", methods=["POST"])
def upload_video():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    # file.save(os.path.join("./Class-265/Project/static", filename))
    with open(os.path.join("./Class-265/Project/static/", filename), "wb") as f:
        f.write(file.read())
    # Code for Project 265 Grayscale start here
    source = cv2.VideoCapture("./Class-265/Project/static" + filename)
    frame_width = int(source.get(3))
    frame_height = int(source.get(4))
    size = (frame_width, frame_height)

    result = cv2.VideoWriter(
        "./Class-265/Project/static/" + "blackandwhite.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        30,
        size,
        0,
    )
    try:
        while True:
            status, frame_image = source.read()
            gray = cv2.cvtColor(frame_image, cv2.COLOR_RGB2GRAY)
            result.write(gray)
            video_file = "blackandwhite.mp4"
    except:
        print("Completed reading all the Frames from the Video")
    # Code for Project 265 end here

    return render_template("upload.html", filename=filename)


# Code for Project 265 download funcion starts here
@app.route("/download")
def download_file():
    converted_video_path = "static/blackandwhite.mp4"
    return send_file(converted_video_path, as_attachment=True)


# Code for Project 265 download funcion ends here


@app.route("/display/<filename>")
def display_video(filename):
    return redirect(url_for("static", filename=filename))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
