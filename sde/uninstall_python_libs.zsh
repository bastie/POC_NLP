#!/bin/zsh 

# uninstall HanTa and numpy
yes | pip3 uninstall numpy HanTa

# uninstall nltk and packages from it
yes | pip3 uninstall nltk click joblib regex tqdm 

# uninstall wheel
yes | pip3 uninstall wheel
