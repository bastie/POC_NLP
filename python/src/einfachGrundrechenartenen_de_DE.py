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
import codecs   # for encodings
import os       # for path
import sys      # for clear exit program

ALL_GOOD = 0

# define relative filepath and print location
theFile = os.path.abspath("./../../../workspace/POC_NLP/text/src/math/einfache_grundrechenarten.de_DE.utf8")
print (theFile)

# define a File to read only in utf-8 coded, read this file complete in var text and close it
textFile = codecs.open(theFile, "r", "utf-8")
text = textFile.read()
textFile.close()

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