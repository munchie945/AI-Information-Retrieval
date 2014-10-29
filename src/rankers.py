'''
Created on Oct 28, 2014

@author: manc
'''
import math

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
            currScore = self.scoringFunction(query, self.documents[i], self.avgDocLength, idf, [termFreq[i] for termFreq in termFreqs])
            indexScoreTuple = (i, currScore)
            scores.append(indexScoreTuple)
        
        # sorts the tuples in descending order based on their scores
        scores.sort(key = lambda x: x[1], reverse = True)
        return scores
    

def length_scoring_function(query, document, documents, idf, termFreqs):
    '''
    Example of a scoring function: returns a numeric score based on the document passed in (in the form of list of strings)
    '''
    docLength = len(document)
    
def bm25_scoring_function(query, document, avgDocLength, idfs, termFreqs):
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
    
    
    
            
        
    
    