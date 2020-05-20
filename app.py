from flask import Flask, render_template, request, redirect, url_for
from detector import Detector
from PIL import Image
import numpy as np
import sys


app = Flask(__name__)
detector = Detector()


@app.route('/classifier')
def home():
    return render_template("frontpage.html")


@app.route('/upload', methods=["POST"])
def classify():
    try:
        image_ = Image.open(request.files['file'].stream)
    except:
        return "Failed to open the image"

    image = np.array(image_)
    predictions = detector.predict(image)

    if predictions:
        return f"Predicted numbers: {' '.join(str(e) for e in predictions)}"
    else:
        return "Oops! Failed to classify numbers on the image provided"


if __name__ == "__main__":
    app.run()
