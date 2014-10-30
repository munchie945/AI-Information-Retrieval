'''
Created on Oct 29, 2014

@author: manc
'''
import math
import os

import Main
import alignment

global allIdfs
allIdfs = {}

def textual_alignment_scoring_function(query, document, avgDocLength, documents, idfs, termFreqs, skipgrams):
    if len(dict) == 0:
        populateIdfs(documents)
    score = []
    p = document
    q = query
    iMax = len(document)
    jMax = len(query)
    scores = ([0] * jMax) * iMax
    maxScore = -1
    for i in range(1, iMax):
        for j in range(1, jMax):
            possScore1 = score[i-1][j-1] + sim(p[i], q[j])
            possScore2 = score[i-1][j] + sim(p[i], None)
            possScore3 = score[i][j-1] + sim(None, q[j])
            scores[i][j] = max(possScore1, possScore2, possScore3, 0)
            if (scores[i][j] > maxScore):
                maxScore = scores[i][j]
    
def populateIdfs(documents):
    nDocs = len(documents)
    allWordFreqs = {}
    result = {}
    for document in documents:
        uniqueWords = []
        for word in document:
            if word not in allWordFreqs:
                '''if the word has never appeared in the corpus before'''
                allWordFreqs[word] = 1
                uniqueWords.append(word)
            elif word not in uniqueWords:
                '''word has been in corpus, but not in curr document before'''
                allWordFreqs[word] += 1
                uniqueWords.append(word)
    for key in allWordFreqs:
        wordFreq = allWordFreqs[key]
        result[key] = math.log((nDocs - wordFreq + 0.5)/(wordFreq + 0.5))
    
    allIdfs = result
    
def sim(term1, term2):
    if (term1 == term2):
        return allIdfs[term1]
    elif (term1 == None):
        return -allIdfs[term2]
    elif (term2 == None):
        return -allIdfs[term1]
    else:
        return -allIdfs[term1]
    