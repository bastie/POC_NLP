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

ALL_GOOD = 0

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
    print (tags)
    
    
# ALL_GOOD = "Oh holy shit"

System.exit(ALL_GOOD);
