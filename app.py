# TODO: added localenv=true, set it for others

from flask import Flask
from fastai.vision.all import load_learner
from utils import is_fluffy
import timm
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/")

def main():
    learn = load_learner("./fluffy-model.pkl")
    
    fluffy,_,probs = learn.predict("./test-img.jpeg")

    output = f"Is this fluffy?: {fluffy}. Probability it's fluffy: {probs[1].item():.6f}"

    return output