""" Webapp for topTen module

Author: Luqman

"""
from flask import Flask
app = Flask(__name__)

import topTen

@app.route('/')
def anyName():
	return topTen.run_all()
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
