'''    
    Hashtag sementation and performance analysis
    Author: Audrey Yang
    Date: October 2, 2022
'''

import nltk
import numpy as np
import io
import re

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
        for i in range(len(word), 0, -1):
            # print("Checking", word[start:i])
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

def answers_list():
    '''
        Formats the "answer key" in such a way so that the MaxMatch results can be compared with it

        Returns: answers, a formatted list of the corect segmentation
    '''
    answers_list = open("testWithAnswers.txt", "r").readlines()
    answers = []
    for i in range(len(answers_list)):
        line = answers_list[i].split(",")
        line[1] = re.sub("\n", "", line[1])
        # ret = line[1].split(" ")
        answers.append(line[1])
    return answers

def WER(guess, answer):
    '''
        Computes the Word Error Rate (WER) between a guess and the correct answer where
        WER is the minimum edit distance divided by the length of the answer (i.e., the normalized
        minimum edit distance)        

        Params: 
            guess: the assumed string segmentation 
            answer: the correct string segmentation which you are comparing guess against
        Returns:
            ret: the normalized minimum edit distance
    '''
    edit_dist = min_edit_dist(guess, answer)
    ret = edit_dist / len(answer)

    return ret 

def main():
    # open the comparison file
    wordbank = open("testHashtags.txt", "r").readlines()

    # "clean up" the wordbank (i.e., remove all "\n")
    words = " ".join(wordbank)
    words = re.sub("\n", "", words)
    wordbank = words.split(" ")

    # MaxMatch with the NLTK corpus
    nltk.download('words')
    NLTKdict = nltk.corpus.words.words()
    print("MaxMatch with NLTK corpus")
    NLTKwords = []

    for word in wordbank:
        NLTKwords.append(max_match(word, NLTKdict))
    
    print(NLTKwords)

    #format for later WER 
    NLTKwerlst = []
    for seg in NLTKwords:
        ret = " ".join(seg)
        NLTKwerlst.append(ret)
    
    #open the Linux Dictionary
    linux_dictionary = io.open("/usr/share/dict/words", 'r', encoding='utf8').readlines()

    # "clean up" the Linux Dictionary (i.e., remove all "\n")
    linuxspliced = " ".join(linux_dictionary)
    linuxspliced = re.sub("\n", "", linuxspliced)
    linux_dictionary = linuxspliced.split(" ")

    #MaxMatch with the Linux Dictionary
    print("\nMatchMax with Linux Dictionary")
    linuxwords = []
    for word in wordbank:
        linuxwords.append(max_match(word, linux_dictionary))
    print(linuxwords)
    
    #format for later WER 
    linuxwerlst = []
    for seg in linuxwords:
        ret = " ".join(seg)
        linuxwerlst.append(ret)

    # open the "rhymes with frugal" dictionary
    rhymesbank = open("bigWordList.txt", "r").readlines()

    # "clean up" the Frugal Rhymes dictionary (i.e., remove all "\n")
    rhymesspliced = " ".join(rhymesbank)
    rhymesspliced = re.sub("\n", "", rhymesspliced)
    rhymesbank = rhymesspliced.split(" ")

    #MaxMatch with the Frugal Rhymes dictionary
    print("\nMatching with Frugal Rhymes dictionary")
    rhymeswords = []

    for word in wordbank:
        rhymeswords.append(max_match(word, rhymesbank))

    print(rhymeswords)
    print()
    
    #format for later WER 
    rhymeswerlst = []
    for seg in rhymeswords:
        ret = " ".join(seg)
        rhymeswerlst.append(ret)

    #get the answer list
    answers = answers_list()
    
    # conduct WER for the NLTK corpus
    NLTKwerage = 0
    for i in range(len(answers)):
        # get the WER for that particular guess and answer
        iWER = WER(NLTKwerlst[i], answers[i])
        NLTKwerage += iWER

        # format and print results
        text = "{}) {}, {}: {}".format(i+1,  NLTKwerlst[i], answers[i], iWER)
        print(text)
    # output average
    NLTKwerage = NLTKwerage / len(NLTKwerlst)
    print("Average WER for NLTK corpus: %f\n"%NLTKwerage)
    
    # conduct WER for the linux dictionary
    linuxwerage = 0
    for i in range(len(answers)):
        # get the WER for that particular guess and answer
        iWER = WER(linuxwerlst[i], answers[i])
        linuxwerage += iWER

        # format and print results
        text = "{}) {}, {}: {}".format(i+1,  linuxwerlst[i], answers[i], iWER)
        print(text)
    # output average
    linuxwerage = linuxwerage / len(linuxwerlst)
    print("Average WER for the Linux dictionary: %f\n"%linuxwerage)

    # conduct WER for the rhymes dictionary
    rhymeswerage = 0
    for i in range(len(answers)):
        # get the WER for that particular guess and answer
        iWER = WER(rhymeswerlst[i], answers[i])
        rhymeswerage += iWER

        # format and print results
        text = "{}) {}, {}: {}".format(i+1,  rhymeswerlst[i], answers[i], iWER)
        print(text)
    # output average
    rhymeswerage = rhymeswerage / len(rhymeswerlst)
    print("Average WER for the \'Rhymes\' dictionary: %f"%rhymeswerage)

main()