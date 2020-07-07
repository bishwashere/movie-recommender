""" Webapp for SimilarTenFile module

Author: Bishwas

"""
from flask import Flask
app = Flask(__name__)

import similarTenFile

@app.route('/<movie_name>')
def recommend(movie_name):
	return similarTenFile.run_all(movie_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
