from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import input_reader
#import scrape_twitter
import os
import numpy as np

# Load model
# from keras.models import Sequential
# from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
# max_fatures = 2000
# embed_dim = 128
# lstm_out = 196
# model = Sequential()
# model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
# model.add(SpatialDropout1D(0.4))
# model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
# model.add(Dense(2,activation='softmax'))
# model.compile(loss = 'sparse_categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
# model_file = os.path.join('Output', 'tweets1_model.h5')
# model.load_weights(model_file)
#from keras.models import load_model
#model = load_model('Output/tweets1_model.h5')
#from keras.preprocessing.text import Tokenizer
#from keras.preprocessing.sequence import pad_sequences

# Sections that pull in libraries for get tokens
#from nltk.tokenize import TweetTokenizer
#from nltk.corpus import stopwords
#from nltk.corpus import words as nltk_words
#from nltk.stem.porter import PorterStemmer
#from pattern.en import suggest, singularize

#stop_words = stopwords.words('english')

# words into dictionary for fast lookup
#engl_words = dict.fromkeys(nltk_words.words(), None)

#initializes porter
#porter = PorterStemmer()

# use strip handle (tweeter) and reduce lenght (haaalooooo -> haaloo)
#tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

#ignore_words = {}
#accepted_words = {}

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/twitter_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    twitter_info = mongo.db.twitter_info.find_one()
    print(twitter_info)
    clean_tweet_list = []
    for key, value in twitter_info.items():

        print(key)
        print(value)
        
        ######## MARTIN TAKE A LOOK HERE #####################
#        max_fatures = 2000

#        tokenizer = Tokenizer(num_words=max_fatures, split=" ")
#        tokenizer.fit_on_texts(value) #NEED TO ENSURE THIS LIBRARY IS BEING FED THE CORRECT INPUT

        #making sequences:
#        X = tokenizer.texts_to_sequences(value) #NEED TO ENSURE THIS LIBRARY IS BEING FED THE CORRECT INPUT
#        X = pad_sequences(X)
       
#        clean_tweet_list.append(((model.predict(X))))

        ######## MARTIN LOOK ABOVE THIS LINE #####################

    return render_template('index.html', twitter_info = twitter_info, cleaned = clean_tweet_list)

# Scrape functions
@app.route('/scrape')
def scraper():
    twitter_info = mongo.db.twitter_info
    twitter_data = scrape_twitter.scrape()
    twitter_info.update({}, twitter_data, upsert = True)
    return redirect("/", code=302)


if __name__ == '__main__':
    app.run(debug=True)