""" Webapp for SimilarTenFile module

Author: Bishwas

"""
from flask import Flask
app = Flask(__name__)

import similarTenFile

@app.route('/')
def home():
	return '404 ERROR !!! <br>Please provide a movie name<br><br>Example:<br><br>http://0.0.0.0:5002/JFK<br><br>http://0.0.0.0:5002/The%20Dark%20Knight%20Rises'

import time
@app.route('/<movie_name>')
def recommend(movie_name):
	start=time.time()
	similarTen = similarTenFile.run_all(movie_name)
	end=time.time()
	return 'Top 10 movies like: %s is <br><br>' % movie_name + similarTen + '<br><br>Execution time: %.2f' % (end-start) + ' seconds'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
