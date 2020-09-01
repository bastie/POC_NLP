'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

from builtins import str
from abc import ABC
from java.lang.UnsupportedOperationException import UnsupportedOperationException
from java.nio.file.Path import Path

class FileSystem(ABC):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    @classmethod
    def getPath (self, first : str, *more) -> Path:
        raise UnsupportedOperationException("Not yet implemented")
        
        
class __vampire_DefaulFileSystem__ (FileSystem):
    '''
    Default implementation of FileSystem with linking to underlying Python
    ''' 
    
    def __init__(self):
        '''
        Constructor
        '''

    @classmethod
    def getPath(self, first : str, *more) -> Path:
        return Path (first, *more)
        