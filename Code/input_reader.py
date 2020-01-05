#!/usr/bin/env python
# coding: utf-8

# Twitter Sentiment Analysis
# Input reader 
# martin hrbac
# 11/18/2019

# Import dependencies
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.corpus import words as nltk_words
from nltk.stem.porter import PorterStemmer
from pattern.en import suggest, singularize

stop_words = stopwords.words('english')

# words into dictionary for fast lookup
engl_words = dict.fromkeys(nltk_words.words(), None)

#initializes porter
porter = PorterStemmer()

# use strip handle (tweeter) and reduce lenght (haaalooooo -> haaloo)
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

ignore_words = {}
accepted_words = {}

def get_tokens(text):
	# text to tokens
	tokens = tknzr.tokenize(text)
	# remove punctuations, words to lower case
	alpha_tokens = [w.lower() for w in tokens if w.isalpha()]
	# do not use stop words
	ns_tokens = [w for w in alpha_tokens if not w in stop_words]
	# stemming
	st_tokens = [porter.stem(t) for t in ns_tokens]
	# only words in dictionary
    
	ow = []
	for w in ns_tokens:
		# remove numbers
		w = ''.join([i for i in w if not i.isdigit()])
		if(w in ignore_words):
			continue;
		# 1) word as is
		if(w in accepted_words):
			ow.append(w)
			continue;
		if(w in engl_words):
			ow.append(w)
			accepted_words[w] = True;
			continue
		# 2) stemmed word
		sw = porter.stem(w)
		if(sw in accepted_words):
			ow.append(sw)
			continue;
		if(sw in engl_words):
			ow.append(sw)
			accepted_words[sw] = True;
			continue
		# 3) singular word
		sw = singularize(w)
		if(sw in accepted_words):
			ow.append(sw)
			continue;
		if(sw in engl_words):
			ow.append(sw)
			accepted_words[sw] = True;
			continue
#        rw = suggest(w)[0]
#        if(rw[1] > 0.5):
#            ow.append(w)
#            accepted_words[w] = True;
#            continue
		ignore_words[w] = True
	return ow
	
	