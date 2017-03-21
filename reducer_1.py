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
            if file_name not in file_list:
            	file_list.append(file_name)
	sys.stdout.write("{0}{1}{2}\n".format(word, sep, file_list))

if __name__ == "__main__":
    reducer()
