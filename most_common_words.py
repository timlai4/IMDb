# Analyze and determine the most common words in the training data set and display their frequencies

import glob
from collections import Counter 

#pattern = 'test/*_0.txt' # Testing
pattern = 'aclImdb/train/*/*.txt'
word_counts = {}
filter_words = ['/><br']

for infile in glob.glob(pattern):
    with open(infile, 'r') as instream:
        review = instream.read()
        for word in review.lower().split():
            for x in filter_words:
                word = word.replace(x,"")
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
                
word_counter = Counter(word_counts)
for word, count in word_counter.most_common(10): # Prints the 10 most common words with frequencies
    print(word, ": ", count)
