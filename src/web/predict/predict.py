# -*- coding: utf-8 -*-
"""similatTenFile

Author: Taha and Jirom

"""

import pandas as pd
import numpy as np
from surprise import Reader, Dataset, SVD 
from surprise.model_selection import cross_validate


def preprocessing():
	movierating = pd.read_csv('dataset/ratings_small.csv')
	return movierating

def svd(movierating, input_user_id, input_movie_id):
	reader = Reader(rating_scale=(1, 5))
	data = Dataset.load_from_df(movierating[['userId', 'movieId', 'rating']], reader)
	
	svd= SVD()

	# Train our dataset
	trainset = data.build_full_trainset()
	svd.fit(trainset)

	validation = cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5)

	# What rating would userId=3 give for movieId 500
	# this is helpful to estimate how a user could rate a movie based on his/her prevous ratings
	rating = str(svd.predict(int(input_user_id), int(input_movie_id)).est)
	return rating

def run_all(input_user_id, input_movie_id):
    movierating = preprocessing()
    return(svd(movierating, input_user_id, input_movie_id))
