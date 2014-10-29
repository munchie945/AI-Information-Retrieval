'''
Created on Oct 28, 2014

@author: manc
'''

import os
import string
import rankers
from rankers import nWordsScoringFunction

def getFiles(fileNames):
    corpus = []
    for fileName in fileNames:
        currFile = open('../corpus/' + fileName, 'r')
        fileString = currFile.read()
        fileString = fileString.lower()
        fileString = fileString.replace('\n', '')
        fileString = fileString.translate(None, string.punctuation)
        fileString = fileString.split(' ')
        corpus.append(fileString)
    return corpus

def printResults(scores, fileNames):
    maxResults = 10
    for i in range(maxResults):
        index, score = scores[i]
        if (scores > 0):
            print fileNames[index], score
        else:
            break

if __name__ == '__main__':
    fileNames = os.listdir('../corpus')
    corpus = getFiles(fileNames)
    ranker = rankers.DocumentRanker(nWordsScoringFunction, corpus)
    scores = ranker.rankDocuments(None)
    printResults(scores, fileNames)
