'''
Created on Oct 28, 2014

@author: manc
'''

class DocumentRanker(object):
    '''
    classdocs
    '''

    def __init__(self, scoringFunction, documents):
        self.scoringFunction = scoringFunction
        self.documents = documents
        
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
        scores = []
        for i in range(len(self.documents)):
            currScore = self.scoringFunction(query, self.documents[i])
            indexScoreTuple = (i, currScore)
            scores.append(indexScoreTuple)
        
        # sorts the tuples in descending order based on their scores
        scores.sort(key = lambda x: x[1], reverse = True)
        return scores

def length_scoring_function(query, document):
    '''
    Example of a scoring function: returns a numeric score based on the document passed in (in the form of list of strings)
    '''
    return len(document)
            
        
    
    