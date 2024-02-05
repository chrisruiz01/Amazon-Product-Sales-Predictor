import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.layers import Embedding
from keras.preprocessing import sequence
from keras.models import load_model
# from tensorflow.keras.preprocessing import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

max_len = 32

# model = load_model('common/model.h5')
model = load_model('common/model.h5')

# with open("common/X_tokenizer.pickle", 'rb') as file:
with open("common/X_tokenizer.pickle", 'rb') as file:
    tokenizer = pickle.load(file)

def preprocess(text):
    sequences = tokenizer.texts_to_sequences(text)
    padded_sequences = pad_sequences(sequences, maxlen=max_len)
    return padded_sequences

def get_predictions(text):
    X = preprocess(text)
    y = model.predict(X)
    # convert predictions to a list (if they are not already)
    predictions = y.tolist()
    return predictions