'''    
    Return all words with a given prefix
    Author: Audrey Yang
    Date: September 15, 2022
'''

import re
# import nltk

def find_prefix(word, words):
    text = " ".join(words)
    print(word)
    r = re.findall(r"\b" + word, text)

    return r

def test_case():
    # haiku = "Row row row your boat. Rowing gently down the stream. Life is so extreme."
    haikuTokens = ['Row', 'row', 'row', 'your', 'boat', '.', 'Rowing', 'gently', 'down', 'the', 'stream', '.', 'Life', 'is', 'so', 'unbelievable', '.','unappetizing', 'toastbun']
    usage = find_prefix('un', haikuTokens)
    print(usage)
    print(len(usage))

test_case()