from flask import Flask, request, jsonify, render_template, json
from flask_cors import CORS
from movie_recommendation import *
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/")
def getModel():
    return render_template('base.html')

@app.route('/', methods=['GET','POST'])
def recommend_movies():
    if request.method == 'POST':
        movie_name = request.form['movie']
        result = results(movie_name)
        # recommendations = jsonify(result)
        recommendations = get_name(result)
    return render_template('show.html', movies = recommendations)

if __name__ == '__main__':
    app.run(debug = True)