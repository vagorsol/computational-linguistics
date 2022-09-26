'''    
    Word and sentence segmentation
    Author: Audrey Yang
    Date: September 25, 2022
'''

import re
from nltk.corpus import gutenberg

def sentence_split(text):
    # split sentences
    split_text = re.split(r'(?<=[\.!?\"])\s\s+', text)

    # then, split each sentences
    ret = [[] for x in range(len(split_text))] 
    i = 0

    for sent in split_text:
        ret[i] = word_split(sent)
        i += 1

    return ret
    

def word_split(text):
    #split string by words
    print(text)
    split_text = re.split(r"([^\w])", text)

    # parse out spaces
    ret = [word for word in split_text if word != " " and word != "" and word != "\n" and word != "\t"]
    print(ret)
    return ret

def test():
    print("Own sentence splitter test:")
    text = gutenberg.raw("austen-emma.txt")
    ret = sentence_split(text)
    print(ret[:10])

    # test_txt = "This is a test string, with lots of: punctuations; in it?!."
    # word_split(test_txt)

    compare_sent = gutenberg.sents("austen-emma.txt")
    print(compare_sent[:10]) 

    # compare_words = gutenberg.words("austen-emma.txt")
    # print(compare_words[:50])
    

test()