'''
    Stochastic POS Tagger
    Name: Audrey Yang
    Date: October 29, 2022
'''

import nltk 
import nltk.tag

# open and tokenize the sample texts (into sentences)
cs_text = open("CS.txt", "r").read()
# print(cs_text)
cs_words = nltk.word_tokenize(cs_text)
print(cs_words)

tagging_dictionary = {}
for(word, tag) in cs_words:
    if tag not in tagging_dictionary:
        tagging_dictionary[tag] = 1
    else: 
        tagging_dictionary[tag] += 1

tags = [tag for (word, tag) in tagging_dictionary]

tagDist = nltk.FreqDist(tags)

uTagr = nltk.UnigramTagger()
        