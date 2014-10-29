'''
Created on Oct 28, 2014

@author: manc
'''

import os
import string

def getFiles():
    listOfFileNames = os.listdir('../corpus')
    corpus = []
    for fileName in listOfFileNames:
        currFile = open('../corpus/' + fileName, 'r')
        fileString = currFile.read()
        fileString = fileString.lower()
        fileString = fileString.replace('\n', '')
        fileString = fileString.translate(None, string.punctuation)
        fileString = fileString.split(' ')
        corpus.append(fileString)
    return corpus

if __name__ == '__main__':
    corpus = getFiles()