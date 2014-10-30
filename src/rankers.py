'''
Created on Oct 28, 2014

@author: manc
'''
import math
import re

class DocumentRanker(object):
    '''
    classdocs
    '''

    def __init__(self, scoringFunction, documents):
        self.scoringFunction = scoringFunction
        self.documents = documents
        self.nDocs = len(documents)
        self.docLengths = [len(document) for document in documents]
        self.avgDocLength = sum(self.docLengths) / float(self.nDocs)
        
        
    def rank_documents(self, query):
        '''
        Takes in:
        query: items to match in the documents, as a list of strings (punctuation stripped etc.)
        documents: a list of documents, where each document is represented as a list of strings (with punctuation etc. removed), and a query to match
        Returns:
        a list of index-score tuples, sorted in descending order of score
            The tuples are in the form (index, score), where:
            index = index of that document in in the list of documents passed in
            score = score of that document, from the scoring function passed in
        '''
        
        '''
        for skipgram, k = 5
        '''
        k = 5
        docSkipGrams = []

        
        for document in self.documents:
            docSkipGram = []
            for i in range(len(document)):
                for j in range(i+1, min(len(document), i+k)):
                    docSkipGram.append(document[i] + " " + document[j])
                    docSkipGram.append(document[j] + " " + document[i])
                
            docSkipGrams.append(docSkipGram)
            
        
        '''
        for bm25
        '''
        idf = []
        n = self.nDocs
        termFreqs = []
        for term in query:
            nq = 0
            termFreq = []
            for document in self.documents:
                freq = 0
                if term in document:
                    nq += 1
                    for word in document:
                        if word == term:
                            freq+=1
                termFreq.append(freq)
            termFreqs.append(termFreq)
            
            idf.append(math.log((n - nq + 0.5)/(nq + 0.5)))
            
        
        
        scores = []
        for i in range(len(self.documents)):
            currScore = self.scoringFunction(query, self.documents[i], self.avgDocLength, self.documents, idf, [termFreq[i] for termFreq in termFreqs], docSkipGrams[i])
            indexScoreTuple = (i, currScore)
            scores.append(indexScoreTuple)
        
        # sorts the tuples in descending order based on their scores
        scores.sort(key = lambda x: x[1], reverse = True)
        return scores
    

def length_scoring_function(query, document, avgDocLength, documents, idf, termFreqs, skipgrams):
    '''
    Example of a scoring function: returns a numeric score based on the document passed in (in the form of list of strings)
    '''
    docLength = len(document)
    
def bm25_scoring_function(query, document, avgDocLength, documents, idfs, termFreqs, skipgrams):
    k = 1.5
    b = 0.75
    docLength = len(document)
    
    score = 0
    
    for i in range(len(query)):
        termFreq = termFreqs[i]
        idf = idfs[i]
        weightedDocLength = docLength / float(avgDocLength)
        score += (idf * termFreq * (k + 1)) / (termFreq + k * (1 - b + b * weightedDocLength))
        
    return score
    
    
def skipbigram_scoring_function(query, document, avgDocLength, documents, idfs, termFreqs, skipgrams):
    '''
    skip-bi-gram with k = 5, therefore we will see bigram, 2skip bigram, 3skip, 4skip, and 5skip-bigram
    '''
    k = 5
    querySkipGrams = query
    
    for i in range(len(query)): 
        for j in range(i+1, min(len(query), k)):
            querySkipGrams.append(query[i]+" "+query[j])
            querySkipGrams.append(query[j]+" "+query[i])
    
    
    intersections = len(set(querySkipGrams) & set(skipgrams))
    for words in skipgrams:
        for term in querySkipGrams:
            if term in words:
                intersections+=1
            
            
            
            
             
    scoreP = intersections/float(len(skipgrams))
    scoreQ = intersections/float(len(querySkipGrams))
    if scoreP == 0 or scoreQ == 0:
        score = 0
    else:
        score = 2*scoreP*scoreQ/float(scoreP+scoreQ)
    
    return score
        
    
    