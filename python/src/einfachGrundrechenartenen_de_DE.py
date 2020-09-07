'''
see 
# href="http://www.nltk.org/book/ - Natural Language Processing with Python - Analyzing Text with the Natural Language Toolkit 
'''



# install certifi, nltk, HanTa, numpy with pip3
# import certifi
# certifi.where()
### once in time downloaded all
# import nltk
# nltk.download()
### ERROR 1123 do this...
### /Applications/Python 3.6/Install Certificates.command


# NLP APIs
import nltk     # for NLP 
from HanTa import HanoverTagger as hTagger    # for NLP (Lemma, POS Tagger) - need numpy

# Just another vampire API
from java.nio.file.FileSystems import FileSystems
from java.nio.file.Files import Files
from java.lang.System import System
from java.io.File import File

# HACK: I need before import word2numberi18n the environment => I think a bug in word2numberi18n 
import os
os.environ ["w2n.lang"] = "de" 
from word2numberi18n import w2n


class Calculate :
    
    
    @classmethod
    def main (_ : type):
        calc = Calculate ()
        calc.run()
        
    def simpleCardString2NumberConverter (self,tags : tuple) -> [tuple]:
        result = []

        for index in range(len (tags)) :
            if "CARD" == tags[index][2] :
                if "NN" == tags[index+1] [2]:
                    if tags[index][1].isnumeric() :
                        tags[index] = (tags[index][0],int(tags[index][1]),tags[index][2])
                    else :
                        # convert 
                        tags[index] = (tags[index][0],w2n.word_to_num(tags[index][1]),tags[index][2])
                        pass
                    result.append((tags[index][1],tags[index+1][0]))
        return result
    
    def run (self):

        # define relative filepath
        theFile = File("./../../../workspace/POC_NLP/text/src/math/einfache_grundrechenarten.de_DE.utf8").getCanonicalPath()
        
        
        # read the file complete in var text and print the text
        text = Files.readString(FileSystems.getDefault().getPath(theFile))
        print (text)
        
        # get sentences from nltk for german
        allSentences = nltk.sent_tokenize(text,language='german')
        # iterate over the sentences, print the sentences and 
        # tokenize the sentence in his word before print words and
        # analyse the word typ
        tagger = hTagger.HanoverTagger("morphmodel_ger.pgz")
        for sentences in allSentences:
            sentencesToken = nltk.tokenize.word_tokenize(sentences,language='german')
            tags = tagger.tag_sent(sentencesToken)
            self.simpleCardString2NumberConverter(tags)
         
            #grammar = "NP : {<CARD>*<NN>1}"
            #parser = nltk.RegexpParser (grammar)
            #output = parser.parse(tags)
            #print(output)
            #output.draw()
            
            
        System.exit(0);
        



Calculate.main()
