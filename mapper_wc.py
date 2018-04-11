#!/usr/bin/env python
"""mapper.py"""

import sys
import re
from nltk.corpus import stopwords

def remove_stopwords(word_list):
    processed_word_list = []
    for word in word_list:
        #Converting to lower case in case some are upper case
        word = word.lower()  
        if word not in stopwords.words("english"):
            processed_word_list.append(word)
    return processed_word_list
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', ' ',line)
    line = re.sub("@\\w+", ' ', line )
    line = re.sub("b[\"']RT", ' ', line )
    line =re.sub('[^A-Za-z0-9]+',' ',line)    
    # split the line into words
    unfilteredWords = line.split()
    words = remove_stopwords(unfilteredWords)
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)

