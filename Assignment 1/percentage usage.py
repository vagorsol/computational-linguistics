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

    # \b isn't working the desired way, which'll be a problem in the future but for now it's fine since due to
    # implementation each token is separated by spaces
    r = re.findall(r" " + word + " ", text)
 
    return len(r) / len(words)

def test_case():
    # haiku = "Row row row your boat. Rowing gently down the stream. Life is so extreme."
    haikuTokens = ['Row', 'row', 'row', 'your', 'boat', '.', 'Rowing', 'gently', 'down', 'the', 'stream', '.', 'Life', 'is', 'so', 'extreme', '.']
    usage = percentage_use('the', haikuTokens)
    print("%.4f" % usage)

test_case()