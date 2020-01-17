# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:12:59 2019

@author: Tim
"""
import glob
import keras

#test_pattern = 'test/*_0.txt' # The directory containing the test data
def read_inputs(train = True, sent = True):
    if train = True:
        if sent = True:
            pattern = 'aclImdb/train/pos/*.txt'
        else:
            pattern = 'aclImdb/train/neg/*.txt'
    else:
        if sent = True:
            pattern = 'aclImdb/test/pos/*.txt'
        else:
            pattern = 'aclImdb/test/neg/*.txt'

    reviews = [] # List which will contain lists of the reviews

    for infile in glob.glob(pattern):
        with open(infile, 'r') as instream:
            for line in instream:
                review = keras.preprocessing.text.one_hot(line, n, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
        reviews.append(review)
    return reviews
    # Still need to create and attach the labels
# def make_inputs(): 
# Here, we should shuffle the data from above and concatenate into one array to feed into NN. 
    
