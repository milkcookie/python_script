#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by milkcooie
#this script is used to get max n seq in fasta file
import sys,os
from optparse import OptionParser
msg_usage = 'usage: python %prog -f in.fasta -o out.fasta -n the head num of seq your want to get'
descr     = 'This script is used to get the head num of seq'
optparser = OptionParser(usage = msg_usage,description = descr)
optparser.add_option('-f','--fasta',dest = 'fasta',help = 'the fasta file you want to stats')
optparser.add_option('-o','--outfasta',dest = 'outfasta',help = 'the out put fasta file')
optparser.add_option('-n','--number', dest = 'number',help = 'the number of seq you want to get')
options,args = optparser.parse_args()
def stats(fasta,outfasta,number):
	ini = open(fasta,'r')
	out = open(outfasta,'w')
	names = []
	dict_num = {}
	dict_seq = {}
	name  = 'name'
	seq   = 'seq'
	num   = 0
	for i in ini:
		if i.startswith('>'):
			dict_seq[name] = seq
			dict_num[name] = num
			name = i.strip()[1:]
			seq  = ''
			num  = 0
			names.append(name)
		else:
			seq   = seq + i 
			num   = num + len(i.strip())
	dict_seq[name] = seq
	dict_num[name] = num
	new_dict = sorted(dict_num.iteritems(), key = lambda asd:asd[1] ,reverse = True)
	outcontig = [m[0] for m in new_dict[0:int(number)]]
	for j in outcontig:
		outline = '>' + j + '\n' + dict_seq[j]
		out.write(outline)
if __name__ == "__main__":
	f = options.fasta
	o = options.outfasta
	n = options.number
	try:
		stats(f,o,n)
	except:
		print "use command: python %s -h to get help"%(__file__)
