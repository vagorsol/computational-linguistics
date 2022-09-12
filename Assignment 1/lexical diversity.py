from nltk.book import *

def lexical_diversity(tokens):
    '''Return lexical diversity of a given list of words (case senseitive)

        Returns: length of list of unique tokens
    '''

    # add only unique instances of elements
    ret = []
    for l in tokens:
        if not(l in ret):
            ret.append(l)
    # ret = [l for l in tokens if not (l in ret)]
    # print(ret)
    return len(ret)

def test_case():
    # haiku = "Row row row your boat. Rowing gently down the stream. Life is so extreme."
    haikuTokens = ['Row', 'row', 'row', 'your', 'boat', '.', 'Rowing', 'gently', 'down', 'the', 'stream', '.', 'Life', 'is', 'so', 'extreme', '.']
    lexdiv = lexical_diversity(haikuTokens)
    print(lexdiv)
    lexdiv_divis = lexdiv / len(haikuTokens)
    print("%.4f" % lexdiv_divis)

def main(): 
    # Lexical Diversity of Sense and Sensibility by Jane Austen
    text2_lexdiv = lexical_diversity(text2) / len(text2)
    print("Text 2 Lexical Diversity: %.4f\%" % text2_lexdiv)

    # Lexical Diversity of Presidental Inaugural Address Corpus                                                                                                                                                                                                                                                                                                                   
    text4_lexdiv = lexical_diversity(text4) / len(text4)
    print("Text 4 Lexical Diversity: %.4f\%" % text4_lexdiv)

    # Lexical Diversity of Chat Corpus
    text5_lexdiv = lexical_diversity(text5) / len(text5)
    print("Text 5 Lexical Diversity: %.4f\%" % text5_lexdiv)
    
    # Lexical Diversity of Monty Python and the Holy Grail
    text6_lexdiv = lexical_diversity(text6) / len(text6)
    print("Text 6 Lexical Diversity: %.4f\%" % text6_lexdiv)

main()