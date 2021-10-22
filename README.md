# Fluffnet

## Intro

Flask API that uses a computer vision model to tell whether an image has something fluffy in it. Go to...

- [here](https://mihailthebuilder.github.io/fluffnet-front/) for the live site
- [here](https://github.com/mihailthebuilder/fluffy-nb) to see how the model was built
- [here](https://github.com/mihailthebuilder/fluffnet-front) for info and source code on the frontend that uses this API

## Table of contents

- [Fluffnet](#fluffnet)
  - [Intro](#intro)
  - [Table of contents](#table-of-contents)
  - [Architecture](#architecture)
  - [Running locally](#running-locally)

## Architecture

The API is a simple Flask project with a single entry point. 

## Running locally

Set up the [frontend](https://github.com/mihailthebuilder/fluffnet-front) and run it locally.

Set up the Python environment.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run this command:

```bash
export FLASK_ENV=development
```

It enables [debug mode](https://flask.palletsprojects.com/en/2.0.x/quickstart/#debug-mode) with hot reload feature, and it enables CORS to localhost.

Start the app:

```bash
flask run
```
