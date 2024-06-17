import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import keras
from keras import layers
import json
import numpy as np

def get_vectorizer(VECTORIZER_METADATA_PATH):
    if VECTORIZER_METADATA_PATH.exists() == False:
        return "Path to the metadata not found"
    
    with open(VECTORIZER_METADATA_PATH, 'r') as infile:
        vectorizer_metadata = json.load(infile)

    vectorizer = layers.TextVectorization(
        max_tokens = vectorizer_metadata['MAX_TOKENS'],
        output_sequence_length = vectorizer_metadata['output_length'],
        vocabulary = vectorizer_metadata['vocabulary']
    )

    return vectorizer

def build_model(MODEL_PATH):
    if MODEL_PATH.exists() == False:
        return "Path to model components not found"
    model = keras.models.load_model(MODEL_PATH)

    return model

def make_prediction(query : str, vectorizer, model):

    vector = tf.expand_dims(vectorizer(query), axis=0)
    prediction = model.predict(vector)
    index = np.argmax(prediction)
    pred = None
    if index == 0:
        pred = "ham"
    else:
        pred = "spam"
    
    return pred



