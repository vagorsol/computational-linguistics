'''    
    Word and sentence segmentation
    Author: Audrey Yang
    Date: September 25, 2022
'''

import re
from nltk.corpus import gutenberg

def sentence_split(text):
    # TODO: get punctuation to stay and deal with Mr./Mrs.
    split_text = re.split(r'(?<=[\.!?\"])\s\s+', text)
    return split_text

    # then, parse the splitted sentences into arr in array and then split by words??

def main():
    text = gutenberg.raw("austen-emma.txt")
    ret = sentence_split(text)
    print(ret[:25], "\n")

    compare_sent = gutenberg.sents("austen-emma.txt")
    print(compare_sent[:10], "\n")

    compare_words = gutenberg.words("austen-emma.txt")
    print(compare_words[:25], "\n")
    

main()