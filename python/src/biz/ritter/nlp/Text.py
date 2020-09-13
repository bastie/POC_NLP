# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE

'''
Created on 13.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

import nltk     # for NLP 

from biz.ritter.nlp import Sentence

from java.nio.file import Path, Files
# HACK: Vampire API 0.2 needed for type IOException
#from java.io import IOException

def iso_639_2_to_nltk_language(x, default=None) -> str:
# TODO: same method defined in Sentence
    return {
        'ger': 'german'
    }.get(x,default)


class Text(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def setSource (self, path : Path):
        self.source = path
    
    def load (self) -> 'Text': # Python 'fearture' self type result, needed for FluentInterfacePattern 
        if None == self.source :
            # HACK: Vampire API 0.2 needed for type IOException
            pass # raise IOException ()
        self.text = Files.Files.readString(self.source)
        return self
    
    def config (self, lang_code_id_iso639_2='ger') -> 'Text':
        self.lang = lang_code_id_iso639_2
        return self
    
    def parse (self) -> 'Text':
        '''
          replace self.text with list of sentences in self
        '''
        # get sentences from nltk for german
        nltk_lang = iso_639_2_to_nltk_language(self.lang, 'german')
        
        allSentences = nltk.sent_tokenize(self.text,language=nltk_lang)
        self.sentences = []
        for nextSentence in allSentences :
            oneSentence = Sentence.Sentence()
            self.sentences.append(oneSentence)
            oneSentence.parse(nextSentence, language=self.lang)

        return self
    
    def run (self, lang_code_id_iso639_2='ger') -> 'Text':
        '''
        run is a collection-method for
        *    load
        *    config
        *    parse
        '''
        self.load() \
            .config(lang_code_id_iso639_2) \
            .parse()
        return self
    
    def toString (self) -> str:
        result = ""
        for nextSentence in self.sentences :
            result +=nextSentence.toString() + " "
        return result.strip()
    

    
