""" Webapp for topTen module

Author: Luqman

"""
from flask import Flask
app = Flask(__name__)

import topTen
import time

@app.route('/')
def anyName():
	start=time.time()
	topTem_demographic = topTen.run_all()
	end=time.time()
	return 'The top 10 movies based on popularity <br>v/(v+m) * R) + (m/(m+v) * C (IMDB formula) is: <br><br>' +topTem_demographic + '<br><br>Execution time: %.2f' % (end-start) + ' seconds'
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
