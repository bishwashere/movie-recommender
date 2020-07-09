# -*- coding: utf-8 -*-
"""topTen

Author: Furkan Ozbudak & Luqman

"""

import pandas as pd
import numpy as np

def preprocessing():
    df2=pd.read_csv('https://raw.githubusercontent.com/bishwashere/mvr/master/src/dataset/movies.csv')

    # ---Demographic Filtering---
    C= df2['vote_average'].mean()

    m= df2['vote_count'].quantile(0.9)

    q_movies = df2.copy().loc[df2['vote_count'] >= m]

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return (v/(v+m) * R) + (m/(m+v) * C)
    
    # Define a new feature 'score' and calculate its value with `weighted_rating()`
    q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
    
    #Sort movies based on score calculated above
    q_movies = q_movies.sort_values('score', ascending=False)

    # Print the top 10 movies
    topTen = q_movies['title'].head(10).tolist()
    topTenString = ""
    
    for index, value in enumerate(topTen):
        topTenString += str(index+1) + '. ' + value + '<br>'

    return topTenString

def run_all():
    top_Ten = preprocessing()
    return top_Ten
