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




class Calculate :
    
    
    @classmethod
    def main (_ : type):
        calc = Calculate ()
        calc.run()
        
    def simpleCardNounExtractor (self,tags : tuple):
#        print (tags)
#        for tag in tags :
#            if "CARD" == tag[2] :
#                print (tag)
        result = []

        for index in range(len (tags)) :
            if "CARD" == tags[index][2] :
                print (tags[index])
                if "NN" == tags[index+1] [2]:
                    print (tags[index][1] + " " + tags[index+1][0])
                    result.append((tags[index][1],tags[index+1][0]))

        pass
    
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
            self.simpleCardNounExtractor(tags)
         
            #grammar = "NP : {<CARD>*<NN>1}"
            #parser = nltk.RegexpParser (grammar)
            #output = parser.parse(tags)
            #print(output)
            #output.draw()
            
            
        System.exit(0);
        

number_system_en = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'point': '.'
}

decimal_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print ()
print (decimal_words)




Calculate.main()
