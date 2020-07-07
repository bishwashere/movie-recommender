""" Webapp for SimilarTenFile module

Author: Bishwas

"""
from flask import Flask
app = Flask(__name__)

import similarTenFile

@app.route('/')
def home():
	return '404 ERROR !!! <br>Please provide a movie name<br><br>Example:<br><br>http://0.0.0.0:5000/JFK<br><br>http://0.0.0.0:5000/The%20Dark%20Knight%20Rises'

@app.route('/<movie_name>')
def recommend(movie_name):
	return similarTenFile.run_all(movie_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
