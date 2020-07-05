from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Available APIs<br>1. /topTen<br>2. /similarTen<br>3. /predictRating"

@app.route('/topTen')
def topTen():
    return 'Display top 10 movies'

@app.route('/similarTen/<movie_id>')
def similarTen(movie_id):
    return 'Display 10 movies similar to ID: %s' % movie_id

@app.route('/similarTen')
def similarTen404():
    return 'Please enter movie ID.<br><br> Example:<br><br> http://127.0.0.1:5000/similarTen/20'

from flask import request
import random
@app.route('/predictRating', methods=['GET'])
def predictRating():
	user_id = request.args.get('user_id', '')
	movie_id = request.args.get('movie_id', '')
	if not(user_id or movie_id):
		return 'Please enter user ID and movie ID.<br><br>Example:<br><br> http://127.0.0.1:5000/predictRating?user_id=999&movie_id=777'
	return 'The USER: %s will rate the MOVIE: %s with rating of: %s' % (user_id, movie_id, random.randint(1, 5))
