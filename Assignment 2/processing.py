'''    
    Word and sentence segmentation
    Author: Audrey Yang
    Date: September 25, 2022
'''

import re
import nltk
from nltk.corpus import gutenberg
from nltk.corpus import inaugural 

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
    ''' Given a body of text, tokenize it
        Params: text, the body of text to tokenize
        Returns: the text, tokenized
    '''

    # sub "-" with " "
    ret = re.sub("-", " ", text)

    #sub punct
    ret = re.sub(",", "", ret)
    ret = re.sub(";", "", ret)
    ret = re.sub("\'", "", ret)
    ret = re.sub("\"", "", ret)

    return ret

def word_count(text):
    '''
        Returns number of words in a body of text (defined: any sequence of letters)
        Param: text, body of text to count words of
        Return: number of words
    '''

    # convert the input into a regex-readable format
    re_compliant = " ".join(text)

    words = re.findall(r"[\w]+([\s]|[^\w])", re_compliant)

    return len(words)

def test():
    ''' Testing Functions
    '''
    text = gutenberg.raw("austen-emma.txt")
    #print(text)
    ret = sentence_split(text[:1000])
    
    #print("output")
    # print(ret[:10])

    test_txt = "This is a test string, with lots of: punctuations; \" \' in it?!."
    print(test_txt)
    i = word_count(test_txt)
    print(i)
    output = tokenize(test_txt)
    print(output)
    # word_split(test_txt)
    #print()

    # compare_sent = gutenberg.sents("austen-emma.txt")
    # print(compare_sent[:10]) 

    # compare_words = gutenberg.words("austen-emma.txt")
    # print(compare_words[:50])  

def main(): 
    # JANE AUSTEN CORPUS   
    text = gutenberg.raw("austen-emma.txt")
    print("Austen Text: ")

    # raw text numbers
    print("Raw Text")
    sentences = gutenberg.sents("austen-emma.txt")
    print(len(sentences)) 

    words = gutenberg.words("austen-emma.txt")
    print(len(words))

    print() 

    # get my segementer numbers
    print("My Segmentation/Tokenizer")
    sentences = sentence_split(text)

    # get word count
    wc = 0
    for line in sentences:
        wc += word_count(line)

    print("Word Count:")
    print(wc)
    print("Sentence Count:")
    print(len(sentences))
    
    print()
    # get NTLK numbers
    print("NLTK Tokenizer")
    words = nltk.word_tokenize(text)
    print("Word Count:")
    print(len(words))

    sentences = nltk.sent_tokenize(text)
    print("Sentence Count:")
    print(len(sentences))

    # INAUGRUAL CORPUS
    print("\nInaugural Text: ")
    inaugural_text = "2021-Biden.txt"
    text = inaugural.raw("2021-Biden.txt")
    
    # raw text numbers
    print("Raw Text")
    sentences = inaugural.sents("2021-Biden.txt")
    print(len(sentences)) 

    words = inaugural.words("2021-Biden.txt")
    print(len(words))

    print() 

    # get my segementer numbers
    print("My Segmentation/Tokenizer")
    sentences = sentence_split(text)

    # get word count
    wc = 0
    for line in sentences:
        wc += word_count(line)

    print("Word Count:")
    print(wc)
    print("Sentence Count:")
    print(len(sentences))
    
    print()
    # get NTLK numbers
    print("NLTK Tokenizer")
    words = nltk.word_tokenize(text)
    print("Word Count:")
    print(len(words))

    sentences = nltk.sent_tokenize(text)
    print("Sentence Count:")
    print(len(sentences))
    
main()