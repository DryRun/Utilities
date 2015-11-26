#!/usr/bin/python
#
#	Layout file generation script
#	Generates .py file like hcal-layouts.py
#

import sys

def create_header(f):
	l = "#\n#	HCAL DQM Layouts\n#\n\n"
	l += "if __name__=='__main__':\n"
	l += "	class DQMItems:\n"
	l += "		def __init__(self, layout):\n"
	l += "			print layout\n"
	l += "	dqmitems = {}\n\n"
	l += "def hcallayout(i, p, *rows):\n"
	l +="	i['Hcal/Layouts/' + p] = DQMItem(layout=rows)\n\n"
	f.write(l)

def create_layout(f, l, name, n, m):
	x = ""
	for i in range(n):
		x += "["
		for j in range(m):
			x += "{"

			x += "'path' : '%s', 'description' : '%s'" % (l[i][j][0],
				l[i][j][1])

			if j==m-1:
				x += "}"
			else:
				x += "},"
		if i==n-1:
			x += "]"
		else:
			x += "],"
			
	s = "hcallayout(dqmitems, '%s', %s)\n\n" % (name, x)
	f.write(s)

def main(f, inp):
	create_header(f)
	lines = inp.readlines()
	il = 0
	while il< len(lines):
		if lines[il]=="" or lines[il]=="\n":
			il+=1
			continue
		if lines[il][0:6]=="layout":
			name = lines[il][7:]
			n = int(lines[il+1].split()[0])
			m = int(lines[il+1].split()[1])
			v = [[["", ""] for jj in range(m)]for ii in range(n)]
			for i in range(n):
				for j in range(m):
					l = lines[il+2+j+i*m]
					v[i][j] = l.split(":")
					v[i][j][1] = "Hcal/"+v[i][j][1].rstrip("\n")
			create_layout(f, v, name, n, m)
		else:
			print "line:",lines[il]
			print "Something is wrong!"
		il+=2+n*m

if __name__=="__main__":
	print "Generating..."
	
	f = open(sys.argv[1], "w")
	inp = open(sys.argv[2])
	main(f, inp)


