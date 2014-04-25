import collections;
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

def bag_of_words(words):
	return dict([(word, True) for word in words])

train_feats =[];
test_feats=[];
#print(movie_reviews.categories()); #list categories
#There are 1000 positive files and 1000 negative files
for label in movie_reviews.categories():
	#print [label]; #display neg,pos
	i=0;
	for fileid in movie_reviews.fileids([label]):
		i=i+1;
		words=movie_reviews.words(fileid);
		bag=bag_of_words(words);
		features=[bag,label];
		if i < 750:
			train_feats.append(features);
		else:
			test_feats.append(features);
#print len(train_feats);
classifier = NaiveBayesClassifier.train(train_feats); #Naive bayes classifier
#test the data
posi=bag_of_words(['kate','winslet','is','accessible']);
nega=bag_of_words(['the','plot','was','ludicrous']);
print classifier.classify(nega);
print classifier.classify(posi);
#display accuracy
print(accuracy(classifier,test_feats));
