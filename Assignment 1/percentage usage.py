'''    
    Returns the percentage use of a given word in a text
    Author: Audrey Yang
    Date: September 12, 2022
'''
import re
from nltk.book import *

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

def main():
    # Usage of 'the' in Sense and Sensibility by Jane Austen
    text2_theusage = percentage_use('the',text2)
    print("2 Usage of 'the' in Text: %.4f" % text2_theusage)

    # Usage of 'the'" in Presidental Inaugural Address Corpus                                                                                                                                                                                                                                                                                                                   
    text4_theusage = percentage_use('the', text4)
    print("Text 4 Usage of 'the' in Text: %.4f" % text4_theusage)

    # Usage of 'the'" inChat Corpus
    text5_theusage = percentage_use('the', text5)
    print("Text 5 Usage of 'the' in Text: %.4f" % text5_theusage)
    
    # Usage of 'the'" in Monty Python and the Holy Grail
    text6_theusage = percentage_use('the', text6)
    print("Text 6 Usage of 'the' in Text: %.4f" % text6_theusage)

main()