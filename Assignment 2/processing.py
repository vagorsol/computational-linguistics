'''    
    Word and sentence segmentation
    Author: Audrey Yang
    Date: September 25, 2022
'''

import re
from nltk.corpus import gutenberg

def sentence_split(text):
    ''' Given a body of text, separated them into sentences
        Params: text, the body of text to segment into sentences
        Returns: a list of sentences where each sentence is a list of the words in the sentence
    '''
    # tokenize the text
    tokenized_text = tokenize(text)

    # split sentences
    split_text = re.split(r'((?<=[\.!?\"])\s\s+|[\n]{2})', tokenized_text)

    
    # get lenght of nonempty sentences to initialize the returned array
    count = 0
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
    ''' Given a body of text, separated them into sentences
        Params: text, the body of text to segment into words
        Returns: a list of words in the text
    '''

    #split string by words
    split_text = re.split(r"([^\w])", text)

    # parse out spaces
    ret = [word for word in split_text if word != " " and word != "" and word != "\n" and word != "\t"]

    return ret

def tokenize(text):
    # sub "-" with " "
    ret = re.sub("-", " ", text)
    print(ret)

    #sub punct
    ret = re.sub(",", "", ret)
    ret = re.sub(";", "", ret)
    ret = re.sub("\'", "", ret)
    ret = re.sub("\"", "", ret)

    return ret

def test():
    ''' Testing Functions
    '''
    text = gutenberg.raw("austen-emma.txt")
    #print(text)
    ret = sentence_split(text[:1000])
    #print("output")
    print(ret[:10])

    #test_txt = "This is a test string, with lots of: punctuations; \" \' in it?!."
    # output = tokenize(test_txt)
    # print(output)
    # word_split(test_txt)
    #print()

    compare_sent = gutenberg.sents("austen-emma.txt")
    print(compare_sent[:10]) 

    # compare_words = gutenberg.words("austen-emma.txt")
    # print(compare_words[:50])
    
test()