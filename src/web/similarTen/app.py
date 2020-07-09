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
	output_string=''
	recommendations_series = similarTenFile.run_all(movie_name)
	for index, value in enumerate(recommendations_series):
		output_string = output_string + str(index+1) + '. ' + value + '<br>'
	return output_string

from flask import render_template
@app.route('/api2/<movie_name>')
def recommendObject(movie_name):
	recommendations_series = similarTenFile.run_all(movie_name)
	return render_template('index.html', movie_series=recommendations_series)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
