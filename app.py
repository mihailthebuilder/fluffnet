from flask import Flask, request
from fastai.vision.all import load_learner
from utils import is_fluffy
import timm
from flask_cors import CORS
import os

app = Flask(__name__)

# check if running on local
_is_local = os.environ.get("localenv", default="false")

# only allow specific origins for API requests
origins = "http://localhost:3000*" if _is_local else ""
cors = CORS(app, resources={r"/": {"origins": origins}})

# allow get requests only
@app.route("/")

def main():

    file = request.files


    if "file" in file:
        file = request.files["file"]

        learn = load_learner("./fluffy-model.pkl")
        
        fluffy,_,probs = learn.predict("./test-img.jpeg")

        output = f"Is this fluffy?: {fluffy}. Probability it's fluffy: {probs[1].item():.6f}"

        return output

    else:
        return "No data sent through"