import nltk
import re

# TODO: if it isn't case insensitive well then fuck i guess (i'm pretty sure the answer is "no")
cfg_grammar = nltk.CFG.fromstring(
    """
   S -> NP VP
   NP -> PRN | N NP | Det N | N
   VP -> V | V VP | V NP 
   V -> "is" | "has" |  "swims" |  "flies" | "are" | "have" |  "bite" |  "fly" |  "biped" |  "does" | "walk" |  "bites" |  "walks" |  "does"
   Det -> "A" | "an" | "a" | "all" | "the"
   N ->  "fish" | "animal" | "bird" |  "gills" |  "Mammals" | "animals" |  "Humans" |  "mammals" |  "Socrates" |  "human" |  "Deepak" |  "Dogs" | "Collies" |  "dogs" |  "Rover" |  "collie" |  "Beagles" |  "Snoopy" | "beagle" | "Birds" | "Canaries" | "birds" |  "Tweety" | "canary" | "Parrots" | "Polly"  |  "parrot" | "canines" |  "hair" |  "feathers" |  "Does"
   PRN -> "Who" | "What" | "what"
   """)

sent = "What bites".split()

print(nltk.pos_tag(sent,tagset="universal"))

text = open("Animals.txt", "r").readlines()
for i in range(len(text)):
    text[i] = re.sub("\n", "", text[i]) # removes newlines
    text[i] = re.sub(r'[^\w\s]',"", text[i]) # removes punctuation
words = " ".join(text)
wordlst = words.split(" ")
wordbank = []
for word in wordlst:
    if word not in wordbank:
        wordbank.append(word)
# print(wordbank)