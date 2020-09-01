'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import os
from builtins import str
from java.lang.UnsupportedOperationException import UnsupportedOperationException

class File(object):
    '''
    classdocs
    '''

    separator : str = os.path.sep

    def __init__(self, *params):
        '''
        Constructor
        '''
        if 1 != len(params) :
            raise UnsupportedOperationException() # TODO: implement other java.io.File constructors with 2 params
        if isinstance(params[0], str) :
            self.path_as_string = params[0]
        else :
            raise UnsupportedOperationException() # TODO: implement other java.io.File constructor with URI
        
        
    def getCanonicalPath (self) -> str:
        return os.path.abspath(self.path_as_string)
    