'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from builtins import staticmethod, str
from java.nio.file.Path import Path
import codecs

class Files(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    
    @staticmethod
    def readString (path : Path) -> str:
        '''
        Java 11 like implementation
        see https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/Files.html#readString(java.nio.file.Path) 
        '''
        textFile = codecs.open(path.toString(), "r", "utf-8")
        text = textFile.read()
        textFile.close()
        return text

    