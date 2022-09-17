'''    
    Return all words with a given prefix
    Author: Audrey Yang
    Date: September 15, 2022
''' 

import re
import nltk

def find_prefix(word, words):
    text = " ".join(words)
    
    pref_regex = r"\b" + re.escape(word) +r"[^\s]+"

    r = re.findall(pref_regex, text)

    return r

def test_case():
    # haiku = "Row row row your boat. Rowing gently down the stream. Life is so extreme."
    haikuTokens = ['Row', 'row', 'row', 'your', 'boat', '.', 'Rowing', 'gently', 'down', 'the', 'stream', '.', 'Life', 'is', 'so', 'unbelievable', '.','unappetizing', 'toastbun']
    usage = find_prefix('un', haikuTokens)
    print(usage)
    print(len(usage))


def main():
    wordlist = nltk.corpus.words.words("en")
    un_list = find_prefix("un", wordlist)
    print(un_list[:25])
    print(len(un_list))

main()