# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE

'''
Created on 18.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

from java.lang import Object
from word2numberi18n import w2n

# HACK: I need before import word2numberi18n the environment => I think a bug in word2numberi18n 
import os
os.environ ["w2n.lang"] = "de" 



class Toolkit(Object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    @classmethod
    def iso_639_2_to_nltk_language(x, default=None) -> str:
        return {
            'ger': 'german'
        }.get(x, default)

    @classmethod
    def simpleCardString2NumberConverter (self,tags : tuple) -> [tuple]:
        '''
        Convert tuple zero and one from string to number
        '''
        result = []

        # FIXME: CARD convert only for CARD before Noun ? Perhaps only for my use case!
        for index in range(len (tags)) :
            if "CARD" == tags[index][2] :
                if "NN" == tags[index+1] [2]:
                    if tags[index][1].isnumeric() :
                        tags[index] = (tags[index][0],int(tags[index][1]),tags[index][2])
                    else :
                        # convert 
                        tags[index] = (w2n.word_to_num(tags[index][0]),w2n.word_to_num(tags[index][1]),tags[index][2])
                    result.append((tags[index][1],tags[index+1][0]))
        return result
