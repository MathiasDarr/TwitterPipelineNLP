"""
This file demonstrates how the SentimentAnalyzer class is used to generate a sentiment score for a selection of topics
such as bidne & trump
"""
# !/usr/bin/env python3

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import defaultdict
from nltk.parse.corenlp import CoreNLPDependencyParser

from analysis.nlp.sentiment_analysis import SentimentAnalyzer


def print_sentiments(text, sentiments):
    description = '''With this sentiment analysis method I have defined I attempt to allow for the presence of 
    multiple subjects in the input text.  A naive algorithm would only assign a single composite score.  My idea is 
    to perform dependency parsing to assign a score for each subject.  The sentiment analysis algorithm depends on 
    the presence of keywords who have been identifed as dependencies of the subject (biden or trump in example).  
    Some keywords I would hope wouuld not be neutral are as demonstrated in this example both 'genius' and 'corrupt' 
    seem to be neutral in the vader SentimentIntensityAnalyzer's mind as they appear to have impact on the sentiment 
    score. '''

    print(description)
    print()
    print(text)
    print()
    print(sentiments)


if __name__ == '__main__':
    text = 'Biden is a chump.  Trump is a genius even though he is corrupt.  Biden is a liar'
    sentimentAnalyzer = SentimentAnalyzer(['biden', 'trump'])
    sentiments = sentimentAnalyzer.generate_sentimenet_scores(text)
    print_sentiments(text, sentiments)

    # biden_sentiments = sentiments['biden']
    # trump_sentiments = sentiments['trump']
    #
    # print("The sentiment for {} is {}".format("Biden: {}".format(biden_sentiments)))
    # print("The sentiment for {} is {}".format("Biden: {}".format(trump_sentiments)))