'''
    Stochastic POS Tagger
    Name: Audrey Yang
    Date: October 29, 2022
'''

import nltk 
from nltk.corpus import brown

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

bts = brown.tagged_sents(categories="news", tagset="universal")
bs = brown.sents(categories="news")

# divide the text into train and test sets
n = int(len(bs) * 0.9)
trainset = bts[:n]
testset = bts[n:]
print(len(testset))

# stochastic tagger
dTagr = nltk.DefaultTagger("NOUN")
uTagr = nltk.UnigramTagger(trainset, backoff = dTagr)
biTagr = nltk.BigramTagger(trainset, backoff = uTagr)

print(biTagr.accuracy(testset))

cs_text = open("CS.txt", "r").read()
cs_words = nltk.word_tokenize(cs_text)
print(biTagr.tag(cs_words))

animals_text = open("Animals.txt", "r").read()
animals_words = nltk.word_tokenize(animals_text)
print(biTagr.tag(animals_words))
# TODO: RE backoff tagger and RE itself evaluation