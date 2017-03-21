#!/usr/bin/env python

import sys, os, string

def mapper():
    sep = '\t'
    data = [line.split() for line in sys.stdin]
    for words in data:
        for word in words:
	    remove_punct = lambda x : x not in string.punctuation
            new_word = filter(remove_punct, word)
            new_word_1 = new_word.lower()
	    if len(new_word_1) > 0:
	        filename = os.getenv('map_input_file').split('/')[6] 
	        sys.stdout.write('{0}{1}{2}\n'.format(new_word_1, sep, filename))

if __name__ == "__main__":
    mapper()
