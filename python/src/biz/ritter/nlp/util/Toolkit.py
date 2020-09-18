# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE

'''
Created on 18.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

from java.lang import Object


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
