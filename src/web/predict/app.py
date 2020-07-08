""" Webapp for SimilarTenFile module

Author: Bishwas

"""
from flask import Flask
app = Flask(__name__)

import predict
from flask import request

@app.route('/')
def anyName():
   user_id  = request.args.get('user_id', None)
   movie_id  = request.args.get('movie_id', None)
   return predict.run_all(user_id, movie_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
