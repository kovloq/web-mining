import nltk; 
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
	for category in movie_reviews.categories()
	for fileid in movie_reviews.fileids(category)]
import random;
random.shuffle(documents);# each document consist of thousand words
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words());
#print documents[0];
#print movie_reviews.words();
print len(all_words.keys()[:2000]);
#list(movie_reviews.words(fileid));