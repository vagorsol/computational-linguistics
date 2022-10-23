'''
    Tag Frequency Analysis
    Author: Audrey Yang
    Date: October 23, 2022
'''

import nltk
from nltk.corpus import brown

tagged_words_uni = brown.tagged_words(categories="news", tagset = "universal")
tagged_words_brown = brown.tagged_words(categories="news",)

ttable = nltk.FreqDist()

# get the frequency of each tag
for(word, tag) in tagged_words_brown:
    ttable[tag] += 1

# count the top tags encounted and print in descending order
tags_dict = {}
for tag in ttable.keys():
    tags_dict.update({ttable[tag]:tag}) # this implementation is not universal 
tags_dict_sorted = sorted(tags_dict.keys(), reverse=True)
print("Top 12 Tags in the Brown Tagset:")
i = 1
for tag_val in tags_dict_sorted[:12]:
    print(i, tags_dict[tag_val], tag_val)
    i += 1

print("\nMost Frequent Words for each Tag in Universal Tagset (Top Ten)")
# find 10 most frequent nouns 
noun_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'NOUN':
        noun_table[word+"/"+tag]+=1
print("Most Frequent NOUNS:")
for (word_tag, count) in noun_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent verbs 
verb_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'VERB':
        verb_table[word+"/"+tag]+=1
print("\nMost Frequent VERBS:")
for (word_tag, count) in verb_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent adpositions 
adp_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'ADP':
        adp_table[word+"/"+tag]+=1
print("\nMost Frequent ADPOSITIONS:")
for (word_tag, count) in adp_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent punctuations 
pun_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == '.':
        pun_table[word+"/"+tag]+=1
print("\nMost Frequent PUNCTUATIONS:")
for (word_tag, count) in pun_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent determiners 
det_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == '.':
        det_table[word+"/"+tag]+=1
print("\nMost Frequent PUNCTUATIONS:")
for (word_tag, count) in det_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent adjectives
adj_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'ADJ':
        adj_table[word+"/"+tag]+=1
print("\nMost Frequent ADJECTIVES:")
for (word_tag, count) in adj_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent adverbs
adv_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'ADV':
        adv_table[word+"/"+tag]+=1
print("\nMost Frequent ADVERBS:")
for (word_tag, count) in adv_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent conjunctions
conj_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'CONJ':
        conj_table[word+"/"+tag]+=1
print("\nMost Frequent CONJUNCTIONS:")
for (word_tag, count) in conj_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent pronouns
prn_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'PRON':
        prn_table[word+"/"+tag]+=1
print("\nMost Frequent PRONOUNS:")
for (word_tag, count) in prn_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent particles
part_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'PRT':
        part_table[word+"/"+tag]+=1
print("\nMost Frequent PARTICLES:")
for (word_tag, count) in part_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent (cardinal) numbers
num_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'NUM':
        num_table[word+"/"+tag]+=1
print("\nMost Frequent NUMBERS:")
for (word_tag, count) in num_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent "other" words (e.g., foreign words, typos, abbrevs)
other_table = nltk.FreqDist()
for(word, tag) in tagged_words_uni:
    if tag == 'X':
        other_table[word+"/"+tag]+=1
print("\nMost Frequent OTHER WORDS:")
for (word_tag, count) in other_table.most_common()[:10]:
    print(count, word_tag)