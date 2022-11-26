'''
    A CFG that accepts nad define the sentences in Animals.txt
    Author: Audrey Yang
    Date: November 25, 2022
'''

import nltk
import re

cfg_grammar = nltk.CFG.fromstring(
    """
   S -> NP VP
   S -> Num NP VP
   NP -> PRN | N NP | Det N | N
   VP -> V | V VP | V NP 
   V -> "is" | "has" |  "swims" |  "flies" | "are" | "have" |  "bite" |  "fly" |  "biped" |  "does" | "walk" |  "bites" |  "walks" |  "does"
   Det -> "A" | "an" | "a" | "all" | "the"
   N ->  "fish" | "animal" | "bird" |  "gills" |  "Mammals" | "animals" |  "Humans" |  "mammals" |  "Socrates" |  "human" |  "Deepak" |  "Dogs" | "Collies" |  "dogs" |  "Rover" |  "collie" |  "Beagles" |  "Snoopy" | "beagle" | "Birds" | "Canaries" | "birds" |  "Tweety" | "canary" | "Parrots" | "Polly"  |  "parrot" | "canines" |  "hair" |  "feathers" |  "Does"
   PRN -> "Who" | "What" | "what"
   Num -> "1" | "2" | "3" | "4" | "5" | "Q1" | "Q2" | "Q3" | "Q4" | "Q5"
   """)

# TODO: make the parser (yay) - wait do I need to include the "1." or no??? maybe??? um. Nums i guess
# Also TODO: 1) Parser on base text (woo), 2) Parser on Animals.txt (extended text) 3) parser on own sentences (3 it accepts, 3 it doesn't). Yay.

sents = ["1. A fish is an animal.", "2. A bird is an animal.", "3. A fish has gills.", "4. A fish swims.", 
        "5. A bird flies.", "Q1. What is a fish?", "Q2. Is a fish an animal?", "Q3. Does a fish swim?", "Q4. Does a bird have gills?", "Q5. Does a bird fly?"]

# formatting text
for i in range(len(sents)):
    sents[i] = re.sub("\n", "", sents[i]) # removes newlines
    sents[i] = re.sub(r'[^\w\s]',"", sents[i]) # removes punctuation
print(sents)

# text = open("Animals.txt", "r").readlines()
# # formatting text
# for i in range(len(text)):
#     text[i] = re.sub("\n", "", text[i]) # removes newlines
#     text[i] = re.sub(r'[^\w\s]',"", text[i]) # removes punctuation
# print(text)