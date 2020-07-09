""" Webapp for SimilarTenFile module

Author: Bishwas

"""
from flask import Flask
app = Flask(__name__)

import predict
from flask import request

import time
@app.route('/')
def anyName():
	start=time.time()
	user_id  = request.args.get('user_id', None)
	movie_id  = request.args.get('movie_id', None)
	if not (user_id or movie_id):
		return '404 ERROR !!! <br>Please provide a movie name<br><br>Example:<br><br>http://0.0.0.0:5003?user_id=4&movie_id=400<br><br>http://0.0.0.0:5003?user_id=500&movie_id=1000'
	prediction_score = predict.run_all(user_id, movie_id)
	end=time.time()
	return "User: %s will rate movie: %s as: %s<br><br>" % (user_id, movie_id, prediction_score) + '<br><br>Execution time: %.2f' % (end-start) + ' seconds'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
