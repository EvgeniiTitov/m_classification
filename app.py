from flask import (
    Flask, render_template, request, redirect, url_for, flash, send_file
)
from werkzeug.utils import secure_filename
from detector import Detector
from PIL import Image
import numpy as np
import sys
import os
import random


app = Flask(__name__)
app.config["SECRET_KEY"] = "tercespot"
app.config["UPLOAD_FOLDER"] = r"D:\Desktop\system_output\WATERMETERS\sent_images"
app.config["DETECTOR"] = Detector()

ALLOWED_EXTs = {"png", "jpg", "jpeg"}
LETTERS = list({"ABCBLAHBLAHBLAH69"})
#detector = Detector()


def is_filename_ok(name):
    """
    Checks if the extension of uploaded file is okay
    :param name:
    :return:
    """
    return os.path.splitext(name)[-1].lower() in ALLOWED_EXTs


def generate_new_name(filename):
    """
    Generates a new name for uploaded file
    :param filename:
    :return:
    """
    extension = os.path.splitext(filename)[-1]
    letters = [
        LETTERS[i] for i in [random.randint(0, len(LETTERS) - 1) for j in range(5)]
    ]
    new_name = f"{''.join(letters)}.{extension}"
    new_name = secure_filename(new_name)

    return new_name


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        if "image" not in request.files:
            flash("You haven't uploaded an image. Try again!")
            return redirect(request.url)

        file = request.files["image"]
        if not file:
            flash("You haven't uploaded an image. Try again!")
            return redirect(request.url)

        # Check if the uploaded file's extension can be handled
        if file and is_filename_ok(file.filename):
            # Generate new file name for security reasons
            filename = generate_new_name(file.filename)
            print("New filename:", filename)
            try:
                save_path = os.path.join(
                    app.config["UPLOAD_FOLDER"], filename
                )
                print("Savepath:", save_path)
                file.save(save_path)
                sent = True
            except Exception as e:
                print(f"Failed during image uploading. Error: {e}")
                sent = False

            if sent:
                return redirect(url_for("predict", filename=filename))
            else:
                flash("Something went wrong. Please try again.")
                return redirect(request.url)
        else:
            flash("Wrong filename or extension. Please try another image")
            return redirect(request.url)

@app.route("/images/<filename>", methods=["GET"])
def images(filename):
    """
    :param filename: absolute path on the server to the image
    :return:
    """
    return send_file(
        os.path.join(app.config["UPLOAD_FOLDER"], filename)
    )

@app.route("/predict/<filename>", methods=["GET"])
def predict(filename):

    return render_template("predict.html")

@app.errorhandler(500)
def server_error(error):
    return render_template("error.html"), 500



# @app.route('/upload', methods=["POST"])
# def classify():
#     try:
#         image_ = Image.open(request.files['file'].stream)
#     except:
#         return "Failed to open the image"
#
#     image = np.array(image_)
#     predictions = detector.predict(image)
#
#     if predictions:
#         return f"Predicted numbers: {' '.join(str(e) for e in predictions)}"
#     else:
#         return "Oops! Failed to classify numbers on the image provided"


if __name__ == "__main__":
    app.run()
