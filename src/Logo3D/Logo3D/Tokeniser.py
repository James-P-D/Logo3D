###############################################
# Libraries
###############################################

import sys
import os
import re

###############################################
# tokenise()
###############################################

def tokenise(text, debug_mode):
    tokens = [i for i in re.split(' |_|\n|\r|\t', text.upper()) if i]
    if (debug_mode):
        print("Tokenising....")
        print(tokens)
        print()
    return tokens
