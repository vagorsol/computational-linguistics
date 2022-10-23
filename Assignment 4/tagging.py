'''
    POS Tagger
    Name: Audrey Yang
    Date: October 23, 2022
'''

import nltk 
# import re

# RE tagger
# universal tagset not included: ADP, CONJ, PRT, X (other), PRON
patterns = [
    (r'[\,:;?1]','.') # punctuation
    (r'^-?[0-9]+(.[0-9]+)?$','NUM') # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'DET') # articles
    (r'.*able$','ADJ') # adjectives
    (r'.*ness$', 'NOUN') # nouns (differentiate from adjectives)
    (r'.*ly$','ADV') # adverbs
    (r'.*ing$','VERB') # verb (gerund)
    (r'.ed$','VERB') # verb (simple past) 
    (r'.es$','VERB') # verb (3rd person singular present)   
    (r'.*ould$','VERB') # modal
    (r'.*\'s','NOUN') # possessive noun
    (r'.*', 'NOUN') # noun default
]

reTagr = nltk.RegexpTagger(patterns)

def main():
    # open and tokenize the sample texts (into sentences)
    cs_text = open("CS.txt", "r").read()
    # print(cs_text)
    cs_words = nltk.sent_tokenize(cs_text)
    print(cs_words)

    # animals_text = open("Animals.txt", "r").readlines()
    # print(animals_text)
    # animals_words = nltk.sent_tokenize(animals_text)
    # print(animals_words)

main()