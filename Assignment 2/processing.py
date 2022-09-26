'''    
    Word and sentence segmentation
    Author: Audrey Yang
    Date: September 25, 2022
'''

import re
from nltk.corpus import gutenberg

def sentence_split(text):
    # split sentences
    split_text = re.split(r'((?<=[\.!?\"])\s\s+|[\n]{2})', text)

    count = 0
    # get lenght of nonempty sentences to initialize the returned array
    for line in split_text:
        app_sent = word_split(line)
        if(app_sent != []):
            count +=1

    # then, split each sentences
    ret = [[] for x in range(count)] 
    i = 0

    for line in split_text:
        app_sent = word_split(line)
        if(app_sent != []):
            ret[i] = word_split(line)
            i += 1
    return ret
    

def word_split(text):

    #split string by words
    split_text = re.split(r"([^\w])", text)

    # parse out spaces
    ret = [word for word in split_text if word != " " and word != "" and word != "\n" and word != "\t"]

    return ret

def test():
    text = gutenberg.raw("austen-emma.txt")
    #print(text)
    ret = sentence_split(text[:1000])
    print("output")
    print(ret[:10])

    # test_txt = "This is a test string, with lots of: punctuations; in it?!."
    # word_split(test_txt)
    print()
    compare_sent = gutenberg.sents("austen-emma.txt")
    print(compare_sent[:10]) 

    # compare_words = gutenberg.words("austen-emma.txt")
    # print(compare_words[:50])
    
test()