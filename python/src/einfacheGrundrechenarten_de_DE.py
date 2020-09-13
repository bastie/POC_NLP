# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE


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
from biz.ritter.nlp import Text     # for sentences class type detection

# Just another vampire API
from java.nio.file.FileSystems import FileSystems
from java.lang.System import System
from java.io.File import File

from rdflib import Graph


class Calculate :
    
    
    @classmethod
    def main (_ : type):
        calc = Calculate ()
        calc.run()
        
    def loadRDF (self):
        simpleModel = Graph()
        simpleModel.parse("./../../../workspace/POC_NLP/text/src/math/einfacheGrundrechenarten_de_DE.ttl",format="turtle")
        print("Anzahl: "+str(len(simpleModel)))
    
    def run (self):
        self.loadRDF()

        # define relative filepath
        theFile = File("./../../../workspace/POC_NLP/text/src/math/einfache_grundrechenarten.de_DE.utf8").getCanonicalPath()
        
        
        # read the file complete in var text and print the text
        textEinfacheGrundrechenarten = Text.Text() 
        textEinfacheGrundrechenarten.setSource (FileSystems.getDefault().getPath(theFile))
        textEinfacheGrundrechenarten.run(lang_code_id_iso639_2='ger')
        text = textEinfacheGrundrechenarten.toString()
        print (text)
        
        
         
            # next not working how I want
            #grammar = "NP : {<CARD>*<NN>1}"
            #parser = nltk.RegexpParser (grammar)
            #output = parser.parse(tags)
            #print(output)
            #output.draw()
            
            
        System.exit(0);
        


Calculate.main()
