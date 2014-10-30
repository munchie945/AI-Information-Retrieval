'''
Created on Oct 29, 2014

@author: manc
'''
import math
import os

import Main
import alignment

def textual_alignment_scoring_function(query, document, avgDocLength, documents, idfs, termFreqs, skipgrams, allidfs):
    p = [0] + document
    q = [0] + query
    iMax = len(p)
    jMax = len(q)
    scores = []
    nDocs = len(documents)
    for a in range(iMax):
        row = []
        for b in range(jMax):
            row.append(0)
        scores.append(row)
    maxScore = -1
    for i in range(1, iMax):
        for j in range(1, jMax):
            possScore1 = scores[i-1][j-1] + sim(p[i], q[j], allidfs, nDocs)
            possScore2 = scores[i-1][j] + sim(p[i], None, allidfs, nDocs)
            possScore3 = scores[i][j-1] + sim(None, q[j], allidfs, nDocs)
            bestScore =  max(possScore1, possScore2, possScore3, 0)
            scores[i][j] = bestScore
            if (scores[i][j] > maxScore):
                maxScore = bestScore
    return maxScore
    
def sim(term1, term2, allIdfs, nDocs):
    idf1 = math.log(nDocs)
    idf2 = math.log(nDocs)
    if term1 in allIdfs:
        idf1 = allIdfs[term1]
    if term2 in allIdfs:
        idf2 = allIdfs[term2]
    
    if (term1 == term2):
        return idf1
    elif (term1 == None):
        return 0 - idf2
    elif (term2 == None):
        return 0 - idf1
    else:
        return 0 - idf2
    