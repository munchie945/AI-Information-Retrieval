'''
Created on Oct 28, 2014

@author: manc
'''

import os
import string
import rankers

def get_files(fileNames):
    corpus = []
    for fileName in fileNames:
        currFile = open('../corpus/' + fileName, 'r')
        fileString = currFile.read()
        fileWordArray = convert_to_words(fileString)
        corpus.append(fileWordArray)
    return corpus

def convert_to_words(rawString):
    rawString = rawString.lower()
    rawString = rawString.replace('\n', '')
    rawString = rawString.translate(None, string.punctuation)
    return rawString.split(' ')
    
def print_results(scores, fileNames):
    maxResults = 10
    for i in range(maxResults):
        index, score = scores[i]
        if (scores > 0):
            print str.format('{:<30} {}', fileNames[index], score)
        else:
            break
    print

if __name__ == '__main__':
    corpusFileNames = os.listdir('../corpus')
    corpus = get_files(corpusFileNames)
    
    scoringFunctions = [rankers.skipbigram_scoring_function]
    
    corpusRankers = [rankers.DocumentRanker(scoringFunction, corpus) for scoringFunction in scoringFunctions]
    
    queryFile = open('../queries.txt', 'r')
    queryStrings = queryFile.readlines()
    for queryString in queryStrings:
        query = convert_to_words(queryString)
        print 'Query:', queryString.replace('\n','')
        for ranker in corpusRankers:
            print 'Scoring Function:', ranker.scoringFunction.__name__
            scores = ranker.rank_documents(query)
            print_results(scores, corpusFileNames)
