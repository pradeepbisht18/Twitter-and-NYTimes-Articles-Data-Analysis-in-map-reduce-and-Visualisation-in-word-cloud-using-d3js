# Twitter-and-NYTimes-Articles-Data-Analysis-in-map-reduce-and-Visualisation-in-word-cloud-using-d3js


1. Introduction
We perform an analysis of current topics of interest in USA.
We collect data from Twitter and New York Times articles.
We retrieve data for the following search terms:
a) “trump”
b) “facebook”
c) “china”
2. Environment
We use the following experimentation environment:
Ubuntu v14
Hadoop v2.9
Python v2.6
HTML, Javascript, d3.js

3. Steps
I. Collect Data (execute nyData.py and twitterData.py)
 Twitter
o We use the ‘Tweepy’ package in Python to collect tweets from Twitter.
o We collect approximately 2500 tweets per topic segregated into around 250 files with 10 tweets
each.
o Data stored in twitterData_queryTerm folder
 NYT
o We use the ‘nytimesarticle’ Python wrapper for the New York Times Article Search API.
o We collect 100 articles per topic, with each article in a separate text file.
o Data stored in nyDataFiles_articles_queryTerm folder

II. Run Mapper_wc.py and Reducer_wc.py on Hadoop Python stream
 Input the raw data file-by-file.
 Removing stop words using the ‘stopwords’ package and ‘NLTK’ stop words corpus.
 Clean the data, removing URLs, handles etc.
 Outputting (word, 1).
 Execute reducer_wc.py.
 Outputting (word, count) in a TSV (tab separate values) file.

III. Sort data using sorted_tsv.py
 Sort data and store in sorted_data.csv file.

IV. Visualize word cloud
 Run wordcloud.html to visualize wordclouds for all search terms.

V. Find word co-occurance using “mapper_word_cooccurance.py”
 Take the top 10 words from the sorted word count file.
 Define context: one article for NYT and collection of 10 tweets for Twitter
Find co-occurance of the top 10 words in the context and output ((word1, word2), 1).
Execute the reducer_wc.py file.
Output the ((word1,word2), count).
Sort and output.
