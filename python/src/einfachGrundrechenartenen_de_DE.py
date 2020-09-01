# install certifi, nltk, HanTa, numpy with pip3
# import certifi
# certifi.where()
### once in time downloaded all
# import nltk
# nltk.download()
### ERROR 1123 do this...
### /Applications/Python 3.6/Install Certificates.command

import nltk     # for NLP 
from HanTa import HanoverTagger as hTagger    # for NLP (Lemma, POS Tagger) - need numpy
import os       # for path
import sys      # for clear exit program
from java.nio.file.FileSystems import FileSystems
from java.nio.file.Files import Files

ALL_GOOD = 0

# define relative filepath
theFile = os.path.abspath("./../../../workspace/POC_NLP/text/src/math/einfache_grundrechenarten.de_DE.utf8")

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
    print(sentences)
    sentencesToken = nltk.tokenize.word_tokenize(sentences,language='german')
    print(sentencesToken)
    tags = tagger.tag_sent(sentencesToken)
    print (tags)
    
    
# ALL_GOOD = "Oh holy shit"

sys.exit(ALL_GOOD);