#!/usr/bin/python
#-*- coding:utf-8 --*-
#by milkcookie
import sys,os
from optparse import OptionParser
msg_usage = 'usage: python %prog -i file.fasta -n num_you_want_split'
descr = 'this script is use to split fasta file'
optparser = OptionParser(usage = msg_usage,description = descr)
optparser.add_option('-i','--infasta',dest = 'infile',help = 'input fasta file')
optparser.add_option('-n','--num',dest = 'num', help = 'the number you want to split the fasta')
options,args = optparser.parse_args()
def split_genome(infile,num):
	ini = open(infile,'r')
	seq_dict = {}
	seq = 'seq'
	name = 'name'
	names = []
	for i in ini:
		if i.startswith('>'):
			seq_dict[name] = seq
			name = i.strip()[1:]
			names.append(name)
			seq = ''
		else:
			seq = seq + i
	seq_dict[name] = seq
	n = 1
	b = int(len(names)/(int(num)))
	a = range(0,len(names),int(len(names)/(int(num))))
	print a
	if int(num) > 2:
		for m in a[0:-2]:
			out = open(infile+'_' + str(n),'w')
			n = n + 1
			for k in names[m:m+b]:
				out.write('>' + k + '\n' + seq_dict[k])
		out = open(infile + '_' + str(n),'w')
		for l in names[a[-2]:]:
			out.write('>' + k + '\n' + seq_dict[l])
	else:
		out = open(infile+'_1','w')
		for m in names[0:a[1]]:
			out.write('>' + m + '\n' + seq_dict[m])
		out1= open(infile+'_2','w')
		for n in names[a[1]:]:
			out1.write('>' + n + '\n' + seq_dict[n])
if __name__ == "__main__":
	i = options.infile
	n = options.num
	split_genome(i,n)
