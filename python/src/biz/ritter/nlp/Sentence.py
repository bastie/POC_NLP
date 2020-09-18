# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE

'''
Created on 13.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import nltk
from HanTa import HanoverTagger as hTagger    # for NLP (Lemma, POS Tagger) - need numpy
from java.lang import IllegalArgumentException, UnsupportedOperationException, Object
from biz.ritter.nlp.util import Toolkit


class Sentence(Object):
    '''
    sentence is a wrapper class and part of abstraction layer so long while I don't found the right way
    
    it is used because I do not found sentence class type in POC NLP library
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def parse (self, sentenceText : str, language = 'ger') -> 'Sentence':
        '''
        Parse sentence in the token and tag this
        '''
        nltk_lang = Toolkit().iso_639_2_to_nltk_language(language, 'german')
        # iterate over the sentences, print the sentences and 
        # tokenize the sentence in his word before print words and
        # analyse the word typ
        tagger = hTagger.HanoverTagger("morphmodel_"+language+".pgz")
#        print (sentenceText)
        sentencesToken = nltk.tokenize.word_tokenize(sentenceText,language=nltk_lang)
        tags = tagger.tag_sent(sentencesToken)
        Toolkit().simpleCardString2NumberConverter(tags)
        self.taggedTokens = tags
#        print(self.toString())
#        print (tags)
        self.__analyseClassOfSentence(language)
#        print ("Sentence class: "+self.sentenceClass)
        return self
    
    
    def __analyseClassOfSentence (self, language = 'ger') -> 'Sentence':
        '''
        Simple generic implementation for German is looking to last char.
        It is also allowed in German to change statement to question.
        '''
        # TODO: looking for 3rd party impl to check for question as sentence class
        result = None
        if "ger" == language :
            if len (self.taggedTokens) > 0:
                if "$." ==self.taggedTokens[-1][2]:
                    if "." == self.taggedTokens[-1][0]:
                        result = "statement"
                    elif "!" == self.taggedTokens[-1][0]:
                        result = "request"
                    elif "?" == self.taggedTokens[-1][0]:
                        result = "question"
                    else:
                        raise IllegalArgumentException (message = "Unknown last char '"+str(self.taggedTokens[-1][0])+"' in sentence:\r"+self.toString()) 
        else :
            raise UnsupportedOperationException (message = "Language "+language+ " not yet (fully) implemented.")
        self.sentenceClass = result
    
    def isQuestion (self) -> bool:
        '''
        Is this sentence a question?
        '''
        return "question" == self.sentenceClass

    def toString (self) -> str:
        result = ""
        for tags in self.taggedTokens :
            if "--" == tags[1] :
                result += str(tags[0]) # no space before point, comma, ...
            else :
                result += " " + str(tags[0])
        return result.strip()