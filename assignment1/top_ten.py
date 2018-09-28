#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:58:21 2018

@author: angelpl
"""
import sys
def compute_hashtags(file):
    import json
    hash_dic = dict()
    with open(file, "r") as fp:
        for line in fp.readlines():
            tweet = json.loads(line)
            
            hashtags = get_tweet_hashtags(tweet)
            for ht in hashtags:       
                hash_dic[ht] = 1 if ht not in hash_dic.keys() \
                    else 1 + hash_dic[ht]
        
    return hash_dic

def get_tweet_hashtags(tweet):
    hashtags = []
    try:
        htlist = tweet['entities']['hashtags']
        hashtags = [x['text'] for x in htlist if x['text'].isalnum()]
    except:
        pass
    return hashtags

def main():
    dic = compute_hashtags(sys.argv[1])
    i = 0
    for k,v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        if i>=10:
            break
        print k, v
        i += 1
        
if __name__ == '__main__':
    main()