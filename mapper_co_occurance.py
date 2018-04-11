#!/usr/bin/env python
"""mapper_co_occurance.py"""

import sys
import re
import pandas as pd
from nltk.corpus import stopwords

from operator import itemgetter
import csv
#wordcount = csv.reader(open("data2.txt"), delimiter="\t")

wordcount = pd.read_csv('sorted_data.tsv', sep='\t',header=0)

#get words column
top_rows = wordcount.head(10)
top_words = top_rows.iloc[:,[0]]

#convert dataaframe to list
top_words_arr = top_words.values.tolist()
top_words_list = [str(top_word).strip('[\']') for top_word in top_words_arr]

#filepath = 'nyText_trump_9.txt'  
#with open(filepath) as fp:
#    line = fp.readline()
#    print(line)

for line in sys.stdin:

    # split the line into words
    words = line.split()

    #CODE FOR COUNTING 
    # Build co-occurrence matrix
    for i in range(0,len(words)-1):
        if words[i].lower() in top_words_list:
            for j in range(i+1, len(words)):
                if words[j].lower() in top_words_list:
                    w1, w2 = sorted([words[i].lower(), words[j].lower()])
                    if w1 != w2:
                        print '%s,%s\t%s' % (w1, w2, 1)
