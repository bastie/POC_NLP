#!/bin/zsh 

# we need install wheel first to clear nltk info messages
pip3 install pdoc3

python3 -m pdoc --force --html --output-dir ../python/docs ../python/src/pjdk/

#EOF
