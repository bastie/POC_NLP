# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE

'''
Created on 13.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import nltk
from HanTa import HanoverTagger as hTagger    # for NLP (Lemma, POS Tagger) - need numpy
from java.lang.UnsupportedOperationException import UnsupportedOperationException

def iso_639_2_to_nltk_language(x, default=None) -> str:
# TODO: same method defined in Sentence
    return {
        'ger': 'german'
    }.get(x,default)

# HACK: I need before import word2numberi18n the environment => I think a bug in word2numberi18n 
import os
os.environ ["w2n.lang"] = "de" 
from word2numberi18n import w2n


class Sentence(object):
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
        nltk_lang = iso_639_2_to_nltk_language(language, 'german')
        # iterate over the sentences, print the sentences and 
        # tokenize the sentence in his word before print words and
        # analyse the word typ
        tagger = hTagger.HanoverTagger("morphmodel_"+language+".pgz")
#        print (sentenceText)
        sentencesToken = nltk.tokenize.word_tokenize(sentenceText,language=nltk_lang)
        tags = tagger.tag_sent(sentencesToken)
        self.simpleCardString2NumberConverter(tags)
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
                        # HACK: need IllegalArgumentException in VampireAPI
                        raise UnsupportedOperationException () 
        else :
            raise UnsupportedOperationException (message = "Language "+language+ " not yet (fully) implemented.")
        self.sentenceClass = result
    
    def isQuestion (self) -> bool:
        '''
        Is this sentence a question?
        '''
        return "question" == self.sentenceClass

    def simpleCardString2NumberConverter (self,tags : tuple) -> [tuple]:
        '''
        Convert tuple zero and one from string to number
        '''
        # FIXME: simpleCardString2NumberConverter is not a method of sentence
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

    def toString (self) -> str:
        result = ""
        for tags in self.taggedTokens :
            if "--" == tags[1] :
                result += str(tags[0]) # no space before point, comma, ...
            else :
                result += " " + str(tags[0])
        return result.strip()