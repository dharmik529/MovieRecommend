# import necessary module
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer 
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Read the dataset into a pandas DataFrame
data = pd.read_csv("tags.csv")

# Initialize TfidfVectorizer to convert tags into TF-IDF features
tfid = TfidfVectorizer()

# Create a matrix of TF-IDF features for the tags
vectorTfid = tfid.fit_transform(data['tags']).toarray()
# Compute cosine similarity between each pair of tag vectors using the TF-IDF matrix
similarityTfidfVect = cosine_similarity(vectorTfid)

# Initialize CountVectorizer to count the occurrences of each word in the tags
cv = CountVectorizer(stop_words='english', lowercase=True)

# Create a matrix of count features for the tags
vector = cv.fit_transform(data['tags']).toarray()
# Compute cosine similarity between each pair of tag vectors using the count matrix
similarityCountVect = cosine_similarity(vector)

# Combine the two similarity matrices using element-wise multiplication
res = np.multiply(similarityTfidfVect, similarityCountVect)

# Save the resulting similarity matrix to a binary file using pickle
filename = 'similarity.pkl'
pickle.dump(res, open(filename, 'wb'))
