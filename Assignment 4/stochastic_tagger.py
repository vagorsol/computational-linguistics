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
   (r'.*able$', 'ADJ'), # adjectives
   (r'.*ness$', 'NOUN'), # nouns from adjectives
   (r'.*ly$', 'ADV'), # adverbs
   (r'.*s$', 'NOUN'), # plural noun
   (r'.*ing$', 'VERB'), # gerund
   (r'.*ed$', 'VERB'), # simple past
   (r'.*es$', 'VERB'), # 3rd person singular present
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

# stochastic tagger
dTagr = nltk.DefaultTagger("NOUN")
uTagr = nltk.UnigramTagger(trainset, backoff = dTagr)
biTagr = nltk.BigramTagger(trainset, backoff = uTagr)

print(biTagr.accuracy(testset))

# TODO: RE backoff tagger and RE itself evaluation