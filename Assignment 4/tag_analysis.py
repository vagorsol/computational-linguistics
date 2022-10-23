import nltk
from nltk.corpus import brown

tagged_words = brown.tagged_words(categories="news", tagset = "universal")

ttable = nltk.FreqDist()

# get the frequency of each tag
for(word, tag) in tagged_words:
    ttable[tag] += 1

# count the top tags encounted (there are only 12 tags) and print in descending order
tags_dict = {}
for tag in ttable.keys():
    tags_dict.update({ttable[tag]:tag}) # this implementation is not universal 
tags_dict_sorted = sorted(tags_dict.keys(), reverse=True)
print("Top Tags Encounted, in Descending Order:")
for tag_val in tags_dict_sorted:
    print(tags_dict[tag_val], tag_val)

# TODO: finish getting "10 most used tags of XYZ tag"

# find 10 most frequent nouns 
noun_table = nltk.FreqDist()
for(word, tag) in tagged_words:
    if tag == 'VERB':
        noun_table[word+"/"+tag]+=1
print("\n10 Most Frequent NOUNS:")
for (word_tag, count) in noun_table.most_common()[:10]:
    print(count, word_tag)

# find 10 most frequent verbs 
verb_table = nltk.FreqDist()
for(word, tag) in tagged_words:
    if tag == 'VERB':
        verb_table[word+"/"+tag]+=1
print("\n10 Most Frequent VERBS:")
for (word_tag, count) in verb_table.most_common()[:10]:
    print(count, word_tag)