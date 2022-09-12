'''    
    Returns the percentage use of a given word in a text
    Author: Audrey Yang
    Date: September 12, 2022
'''
import re
# from nltk.book import *

def percentage_use(word, words):
    '''
        Returns the percentage use of a given word in a text
        Params: word, the word you want to find usage percentage of
                words, a lsit of tokens you want to find the usage percentage of word from
        Return:
    '''

    # convert the list of tokens into on string 
    text = " ".join(words)

    # get size of text
    text_size = len(words)

    r = [l for l in text if re.search(" " + word + " ", text)]
    print(r)
 
    return 0

def test_case():
    # haiku = "Row row row your boat. Rowing gently down the stream. Life is so extreme."
    haikuTokens = ['Row', 'row', 'row', 'your', 'boat', '.', 'Rowing', 'gently', 'down', 'the', 'stream', '.', 'Life', 'is', 'so', 'extreme', '.']
    usage = percentage_use('the', haikuTokens)
    print(usage)

test_case()