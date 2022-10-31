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
   (r'of|Of|in|In|for|For|to|To|on|On|at|At|that|That|with|With|by|By|As|as|from|From', 'ADP'), # adpositions
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

# NEWS CORPUS
nts = brown.tagged_sents(categories="news", tagset="universal")

# divide the text into train and test sets
n = int(len(nts) * 0.9)
trainset_news = nts[:n]
testset_news = nts[n:]

# stochastic tagger
dTagr = nltk.DefaultTagger("NOUN")
uTagr = nltk.UnigramTagger(trainset_news, backoff = dTagr)
biTagr = nltk.BigramTagger(trainset_news, backoff = uTagr)

# RE backoff tagger
uREtagr = nltk.UnigramTagger(trainset_news, backoff = reTagr)
biREtagr = nltk.BigramTagger(trainset_news, backoff = uREtagr)

print("News Brown Corpus")
print(f"Bigram Default Tagger Backoff Accuracy: {biTagr.accuracy(testset_news)}")
print(f"Bigram RE Backoff Accuracy: {biREtagr.accuracy(testset_news)}")
print(f"RE Tagger Accuracy: {reTagr.accuracy(testset_news)}")

# FICTION CORPUS
fts = brown.tagged_sents(categories="fiction", tagset="universal")
n = int(len(fts) * 0.9)
trainset_fic = nts[:n]
testset_fic = nts[n:]

# stochastic tagger
dTagr = nltk.DefaultTagger("NOUN")
uTagr = nltk.UnigramTagger(trainset_fic, backoff = dTagr)
biTagr = nltk.BigramTagger(trainset_fic, backoff = uTagr)

# RE backoff tagger
uREtagr = nltk.UnigramTagger(trainset_fic, backoff = reTagr)
biREtagr = nltk.BigramTagger(trainset_fic, backoff = uREtagr)

print("\nFiction Brown Corpus")
print(f"Bigram Default Tagger Backoff Accuracy: {biTagr.accuracy(testset_fic)}")
print(f"Bigram RE Backoff Accuracy: {biREtagr.accuracy(testset_fic)}")
print(f"RE Tagger Accuracy: {reTagr.accuracy(testset_fic)}")

# open and tokenize the sample texts
cs_text = open("CS.txt", "r").read()
cs_words = nltk.word_tokenize(cs_text)

animals_text = open("Animals.txt", "r").read()
animals_words = nltk.word_tokenize(animals_text)