from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
import pandas as pd
import numpy as np
import pickle
import csv
from sklearn.metrics.pairwise import cosine_similarity

# csvfile = "tags.csv"
# f = open(csvfile, 'r')
# data = csv.reader(f)
data = pd.read_csv("tags.csv")

tfid = TfidfVectorizer()

vectorTfid = tfid.fit_transform(data['tags']).toarray()
similarityTfidfVect = cosine_similarity(vectorTfid)

cv = CountVectorizer(stop_words='english', lowercase=True)

vector = cv.fit_transform(data['tags']).toarray()
similarityCountVect = cosine_similarity(vector)

# hash = HashingVectorizer(lowercase=True, stop_words={'english'}, ngram_range=(1,1))

# vectorHash = hash.fit_transform(data['tags']).toarray()
# similarityHashingVect = cosine_similarity(vectorHash)


# COMBINING SIMILARITIES
res = np.multiply(similarityTfidfVect, similarityCountVect)
# res = np.multiply(res, similarityHashingVect)

filename = 'similarity.pkl'
pickle.dump(res, open(filename, 'wb'))