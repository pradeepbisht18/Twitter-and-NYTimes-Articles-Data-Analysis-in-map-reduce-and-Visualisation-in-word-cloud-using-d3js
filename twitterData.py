# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 21:28:05 2018

@author: Karan Hora
"""
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import os.path
import json
import pandas as pd
import matplotlib.pyplot as plt

consumer_key = 'fQnGLvOSirImGrMbBmi8IDrvS'
consumer_secret = 'IVr53aqnjR5cDe4NmbSxmiwSbnHwwSb2Wqh8SBRmNLICfi96Ex'
access_token = "28844151-grLeSTBd70FyHxeco5mOsMkecBp9SHQHROeyx1Zbe"
access_token_secret = "Ksn72dihzRi31itVhigpysO1FDxfD3JLSFfeFbp4hF840"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)

query = "china"

language = "en"

num_tweets = 5000

save_path = 'C:/Users/Karan Hora/Desktop/587 DIC/lab 2/twitterDataFiles_china'

allTweets = []
flag = 10
file_num = 0
try:
    for messages in tweepy.Cursor(api.search, q = query,  lang = language, tweet_mode = 'extended'
                                      ).items(num_tweets):
               
            tweetMessage = str(messages.full_text.encode('ascii', 'ignore'))
            print(tweetMessage)
            allTweets.append(tweetMessage)
            flag = flag - 1       
            while(flag == 0):
                file_num = file_num + 1
                name_of_file = 'twitterText_%s_%d' % (query,file_num)
                completeName = os.path.join(save_path, name_of_file+".txt")          
                twText=open(completeName ,'w')
                for element in allTweets:
                    twText.write(element+'\n')
                twText.close()
                allTweets = []
                flag = 10
   
except:
    pass
