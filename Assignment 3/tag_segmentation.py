'''    
    Hashtag sementation and performance analysis
    Author: Audrey Yang
    Date: October 2, 2022
'''

import numpy as np

def max_match(word, word_list):
    '''
        An implementation of the MaxMatch algorithm, using the Python
        implementation described in class

        Params: 
                word: the set of text you are parsing
                wordlist: the word databank you are using as reference for segmentation
        Returns:
                words: the set of words that were parsed from the text
    '''
    start = 0
    words = []

    while start < len(word):
        match = False
        for i in range(len(words), 0, -1):
            #print("Checking", word[start:i])
            if(word[start:i] in word_list):
                words.append(word[start:i])
                match = True
                start = i 
                break
            if not match:
                words.append(word[start])
                start += 1
    return words

def min_edit_dist(source, target):
    '''
        An implementation of the Minimum Edit Distance algorithm,
        using the psuedocode shown in class

        Params:
            source: the word that is to be "transformed"
            target: the word that source is to be "transformed" into
        Returns:
            D[len(target), len(source)], the minimum edit distance
            
    '''
    # Create a (|x| + 1 * |y| + 1) matrix, D
    D = np.empty((len(source) + 1, len(target) + 1))
    D[0,0] = 0

    # Initialzie the first row + column 
    for i in range(1, len(source) + 1):
        D[i,0] = i
    for i in range(1, len(target) + 1):
        D[0,i] = i

    # Compute the remaining distance D
    for i in range(1,len(source) + 1):
        for j in range(1, len(target) + 1):
            ins_cost = D[i - 1, j] + 1
            del_cost = D[i, j - 1] + 1
            
            #get sub cost
            if target[j - 1] == source[i - 1]:
                sub_cost = D[i - 1, j - 1] + 0
            else:
                sub_cost = D[i - 1, j - 1] + 2
            #find the minimum cost 
            costs = set([ins_cost, del_cost, sub_cost])
            min_cost = min(costs)

            D[i,j] = min_cost 

    return D[len(source), len(target)]

min_ed = min_edit_dist("cat", "cate")
print(min_ed)