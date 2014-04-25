import nltk; 
from nltk.corpus import names
import random

def gender_features2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features

def last_word(word):
	return word[-1];
def gender_features(word):
	features={};#define an array
	features['last_letter']=word[-1];
	#features['length']=len(word);
	#features['first_letter']=word[0];
	return features;
    #return {'last_letter': word[-1]} Featurenya harus dikasi label formatnya harus kaya gini

#print last_word("tes");
#Names ending in a, e and i are likely to be female, while names ending in k, o, r, s and t are likely to be male

names = ([(name, 'male') for name in names.words('male.txt')] +
        [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names);
#laki=names.words('male.txt'); #the length is 2942
#print len(names);#7994
featuresets = [(gender_features(n), g) for (n,g) in names];
#print featuresets;
#get first 500 to train
train_set, test_set = featuresets[500:], featuresets[:500];
#print featuresets.keys();
#get last 500 to test
classifier = nltk.NaiveBayesClassifier.train(train_set); #Naive bayes classifier
#print classifier.classify(gender_features('Neo'));
#print 'accuracy=', nltk.classify.accuracy(classifier, test_set) ;
#classifier.show_most_informative_features(5)

#print gender_features2('dana');