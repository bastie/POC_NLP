'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from builtins import str
import os

class Path(object):
    '''
    classdocs
    '''

    def __init__(self, first : str, *more):
        '''
        Constructor
        '''
        self.path_as_string = first 
        for nextParam in more :
            self.path_as_string += os.path.sep + nextParam # TODO: use pjava.io.File.separator = os.path.sep
        pass
        

        
    def toString (self) -> str:
        return self.path_as_string