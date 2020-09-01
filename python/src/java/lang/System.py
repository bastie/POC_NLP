'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from os.path import sys

class System(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @classmethod
    def exit (self, status : int):
        sys.exit(status)