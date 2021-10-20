from flask import Flask, request
from fastai.vision.all import load_learner, PILImage
from utils import is_fluffy
import timm
from flask_cors import CORS
import os

app = Flask(__name__)

# check if running on local
_is_local = os.environ.get("FLASK_ENV", default="production")

# only allow specific origins for API requests
origins = "http://localhost:3000" if _is_local == "development" else "https://mihailthebuilder.github.io/fluffnet-front"
cors = CORS(app, resources={r"/": {"origins": origins}})

# allow get requests only
@app.route("/",methods=["POST"])

def main():

    files = request.files

    output = {}

    if "image" in files:
        image = request.files["image"]

        learn = load_learner("./fluffy-model.pkl")

        image_processed = PILImage.create(image)
        
        fluffy,_,probs = learn.predict(image_processed)

        output["fluffy"] = fluffy
        output["prob"] = probs[1].item()

    return output