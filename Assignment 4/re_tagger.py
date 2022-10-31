'''
    Regular Expression POS Tagger
    Name: Audrey Yang
    Date: October 23, 2022
'''

import nltk 
# import re

# RE tagger
# universal tagset not included: ADP, CONJ, PRT, X (other), PRON
patterns = [
   (r'[\.,:;?!]', '.'), # punctuation
   (r'^-?[0-9]+(.[0-9]+)?$', 'NUM'), # cardinal numbers
   (r'(The|the|A|a|An|an)$', 'DET'), # articles
   (r'(At|at|On|on|Out|out|Over|over|Per|per|That|that|Up|up|Down|down)$', 'PRT'), # articles
   (r'I|you|You|he|He|she|She|it|It|we|We|they|They|who|Who|what|What', 'PRON'), # personal pronouns
   (r'For|for|and|And|nor|Nor|but|But|or|Or|yet|Yet|so|So', 'CONJ'), # conjunctions 
   (r'is|Is|are|Are|was|Was|were|Were|am|Am|been|Been','VERB'), # verb present singular first person
   (r'of|Of|in|In|for|For|to|To|on|On|at|At|that|That|with|With|by|By|As|as|from|From'), # adpositions
   (r'.*able$', 'ADJ'), # adjectives
   (r'.*ness$', 'NOUN'), # nouns from adjectives
   (r'.*ly$', 'ADV'), # adverbs
   (r'.*s$', 'NOUN'), # plural noun
   (r'.*ing$', 'VERB'), # verb gerund
   (r'.*ed$', 'VERB'), # verb simple past
   (r'.*es$', 'VERB'), # verb 3rd person singular present
   (r'.*ould$', 'VERB'), # modal
   (r'.*\'s', 'NOUN'), # possessive noun
   (r'.*', 'NOUN') # noun default
]

reTagr = nltk.RegexpTagger(patterns)

def main():
    # open and tokenize the sample texts (into sentences)
    # cs_text = open("CS.txt", "r").read()
    # cs_words = nltk.word_tokenize(cs_text)
    # print(cs_words)

    # print(reTagr.tag(cs_words))

    animals_text = open("Animals.txt", "r").read()
    animals_words = nltk.word_tokenize(animals_text)
    # print(animals_words)
    print(reTagr.tag(animals_words))
main()