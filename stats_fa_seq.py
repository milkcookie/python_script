#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by milkcooie
#this script is used to stats every seq length in fasta file
import sys,os
def stats(fasta,length):
	ini = open(fasta,'r')
	out = open(length,'w')
	names = []
	dict_seq = {}
	for i in ini:
		if i.startswith('>'):
			name = i.strip()[1:]
			seq  = ''
			names.append(name)
		else:
			seq  = seq + i
			lens = len(seq)
			dict_seq[name] = lens
	for na in names:
		outline = na + ':' + str(dict_seq[na]) + '\n'
		out.write(outline)
if __name__ == "__main__":
	fasta = sys.argv[1]
	length= sys.argv[2]
	try:
		stats(fasta,length)
	except:
		print "usage: python stats_fa_seq.py fastafile lengthfile"

