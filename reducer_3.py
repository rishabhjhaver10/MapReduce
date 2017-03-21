#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def reducer():
    sep = '\t'
    data = [line.strip().split(sep, 1) for line in sys.stdin]
    for author, group in groupby(data, itemgetter(0)):
        word_list = []
        for author, word in group:
            word_list.append(word)
        word_dict = {}
	for wrd in word_list:
    	    if wrd in word_dict:
                word_dict[wrd] += 1
            else:
                word_dict[wrd] = 1
	sys.stdout.write('{0}{1}{2}\n'.format(author, sep, word_dict))

if __name__ == "__main__":
    reducer()
