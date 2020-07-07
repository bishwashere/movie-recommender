# -*- coding: utf-8 -*-
"""similatTenFile

Author: Luqman and Bishwas

"""

import pandas as pd 
import numpy as np

#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocessing():
    df1=pd.read_csv('credits.csv')
    df2=pd.read_csv('movies.csv')

    df1.columns = ['id','tittle','cast','crew']
    df2= df2.merge(df1,on='id')

    # ---CONTENT BASED---

    #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    df2['overview'] = df2['overview'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df2['overview'])

    #Output the shape of tfidf_matrix
    #tfidf_matrix.shape

    # Import linear_kernel
    from sklearn.metrics.pairwise import linear_kernel

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    #Construct a reverse map of indices and movie titles
    indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

    #Construct a reverse map of indices and movie titles
    indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

    return (df2['title'], cosine_sim, indices)

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, df2_title, cosine_sim, indices):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df2_title.iloc[movie_indices]

def recommend(recommendations_series):
    output_string=''
    for index, value in enumerate(recommendations_series):
        output_string = output_string + str(index+1) + '. ' + value + '<br>'
    return output_string

def run_all(title):
    (df2_title, cosine_sim, indices) = preprocessing()
    recommendations_series = get_recommendations(title, df2_title, cosine_sim, indices)
    return recommend(recommendations_series)