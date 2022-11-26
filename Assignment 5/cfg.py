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
   S -> Num VP NP
   NP -> PRN | N NP | Det N | N
   VP -> V | V VP | V NP 
   V -> "is" | "Is" | "has" | "swim" | "swims" |  "flies" | "are" | "have" |  "bite" |  "fly" |  "biped" |  "does" | "walk" |  "bites" |  "walks" |  "does"
   Det -> "A" | "an" | "a" | "all" | "the"
   N ->  "fish" | "animal" | "bird" |  "gills" |  "Mammals" | "animals" |  "Humans" |  "mammals" |  "Socrates" |  "human" |  "Deepak" |  "Dogs" | "Collies" |  "dogs" |  "Rover" |  "collie" |  "Beagles" |  "Snoopy" | "beagle" | "Birds" | "Canaries" | "birds" |  "Tweety" | "canary" | "Parrots" | "Polly"  |  "parrot" | "canines" |  "hair" |  "feathers" |  "Does"
   PRN -> "Who" | "What" | "what"
   Num -> "1" | "2" | "3" | "4" | "5" | "Q1" | "Q2" | "Q3" | "Q4" | "Q5"
   """)

parser = nltk.RecursiveDescentParser(cfg_grammar)

# Reformats text to be parsable through the grammar
def format_sents(sents):
    for i in range(len(sents)):
        sents[i] = re.sub("\n", "", sents[i]) # removes newlines
        sents[i] = re.sub(r'[^\w\s]',"", sents[i]) # removes punctuation
    return sents


sents = ["1. A fish is an animal.", "2. A bird is an animal.", "3. A fish has gills.", "4. A fish swims.", 
        "5. A bird flies.", "Q1. What is a fish?", "Q2. Is a fish an animal?", "Q3. Does a fish swim?", "Q4. Does a bird have gills?", "Q5. Does a bird fly?"]

sents = format_sents(sents)
# print out the parse tree of the sentence
for i in range(len(sents)):
    for p in parser.parse_all(sents[i].split()):
        print(p)

text = open("Animals.txt", "r").readlines()
text = format_sents(text)
# checking to see if there is a sentence in Animals.txt that the parser can't parse
for i in range(len(text)):
    if parser.parse_all(text[i].split()) is None:
        print(f"{text[i]}")
