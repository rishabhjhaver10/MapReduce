#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def reducer():
    sep = '\t'
    data = [line.strip().split(sep, 1) for line in sys.stdin]
    for word, group in groupby(data, itemgetter(0)):
        file_list = []
        for word, file_name in group:
            file_list.append(file_name)
        file_dict = {}
	for file_name_1 in file_list:
    	    if file_name_1 in file_dict:
                file_dict[file_name_1] += 1
            else:
                file_dict[file_name_1] = 1
	sys.stdout.write('{0}{1}{2}\n'.format(word, sep, file_dict))

if __name__ == "__main__":
    reducer()
