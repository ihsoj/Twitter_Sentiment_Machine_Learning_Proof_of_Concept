
# Twitter Sentiment Analysis
# Final Project
# 11/20/2019

# Code requies running mongodb with twitter_app database with twitter_info collection

# system modules
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import os
import numpy as np

# For model
import tensorflow as tf
from keras.models import load_model
#from keras.models import Sequential
#from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
#from threading import Thread

# user modules
import sys
sys.path.insert(0,  os.path.join('.', 'Code'))
import input_reader
import scrape_twitter

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/twitter_app"
mongo = PyMongo(app)

# Define what to do when a user hits the index route
@app.route("/")
def home():

	twitter_info = mongo.db.twitter_info.find_one()
	#print(twitter_info)
	clean_tweet = {}
	twitter_text = {}
	
	# !!! enabeling any of the model will crash with : AttributeError: '_thread._local' object has no attribute 'value' 
	#trained_model = build_model()
	#load_keras_model()

	if twitter_info is not None:
		for tweet in twitter_info:
			if(tweet != '_id'):
				twitter_text[tweet] = twitter_info[tweet]
				tokens = input_reader.get_tokens(str(twitter_info[tweet]))
				clean_tweet[tweet] = ' '.join(tokens)

	return render_template('index.html', twitter_text = twitter_text, cleaned = clean_tweet)

# Scrape functions
@app.route('/scrape')
def scraper():
    twitter_info = mongo.db.twitter_info
    twitter_data = scrape_twitter.scrape()
    twitter_info.update({}, twitter_data, upsert = True)
    return redirect("/", code=302)


def load_keras_model():
	model_file = os.path.join('Output', 'tweets1_model.h5')
	global model
	model = load_model(model_file)
	# Required for model to work
	global graph
	graph = tf.get_default_graph()
	

def build_model():

	max_fatures = 2000

	embed_dim = 128
	lstm_out = 196

	Xshape1 = 35 # this is hardcoded (matches value used during training), need to be properly

	model = Sequential()
	model.add(Embedding(max_fatures, embed_dim,input_length = Xshape1))
	model.add(SpatialDropout1D(0.4))
	model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
	model.add(Dense(2,activation='softmax'))
	model.compile(loss = 'sparse_categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])

	# load trained data
	model_file = os.path.join('..', 'Output', 'tweets1_model.h5')
	model.load_weights(model_file)

	return model

@app.route("/about")
def about():
    print("Final Project")
    return "Final Project!"

if __name__ == "__main__":
    app.run(debug=True)
