'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from builtins import staticmethod
from java.nio.file import FileSystem
from java.nio.file.FileSystem import __pjdk_DefaulFileSystem__

class FileSystems(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def getDefault () -> FileSystem:
        return __pjdk_DefaulFileSystem__()