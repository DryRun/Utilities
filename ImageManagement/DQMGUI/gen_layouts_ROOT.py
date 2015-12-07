#!/usr/bin/python
#
#	Layout file generation script
#	Generates .py file like hcal-layouts.py
#

import sys

parserDir = "/Users/vk/software/HCALDQM/Utilities/Parser"
sys.path[len(sys.path):] = [parserDir]
import Parser

def create_header(f):
	"""
	Generate the header of the layout file
	"""
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
	""" 
	Create a single layout. Use name, nrow, ncol, and list of path+name and description
	"""
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

def create_singlelayout(f, lname, pathname, desc):
	"""
	Create a layout out of a single plot
	"""

	x = "[{"
	x += "'path' : '%s', 'description' : '%s'" % (pathname, desc)
	x += "}],"
	s = "hcallayout(dqmitems, '%s', %s)\n\n" % (lname, x)
	f.write(s)

def create_fromTxt(f, inName):
	"""
	Generate Layout py file from a Txt File, by specifying all the layouts in a txt file. See example
	"""
	inp = open(inName)
	create_header(f)
	lines = inp.readlines()
	il = 0
	while il< len(lines):
		if lines[il]=="" or lines[il]=="\n":
			il+=1
			continue
		if lines[il][0:6]=="layout":
			name = lines[il][7:].rstrip()
			n = int(lines[il+1].split()[0])
			m = int(lines[il+1].split()[1])
			v = [[["", ""] for jj in range(m)]for ii in range(n)]
			for i in range(n):
				for j in range(m):
					l = lines[il+2+j+i*m]
					v[i][j] = l.split(":")
					v[i][j][1] = v[i][j][1].rstrip("\n")
					v[i][j][0] = "Hcal/"+v[i][j][0]
			create_layout(f, v, name, n, m)
		else:
			print "line:",lines[il]
			print "Something is wrong!"
		il+=2+n*m

def create_fromROOT(pyOutFile, rootFileName):
	"""
	Create Layout py file from a ROOT file by using Parser utility
	"""

	#	common definitins
	dictTasks = {"DigiTask" : "DIGI", "RawTask" : "RAW", "TPTask" : "TP",
		"RecHitTask" : "RECO"}
	descdigitiming = "Nominal fC weighted Time A    verage. Cuts are applied on the Amplitude"
	descrecotiming = "RECO Timing in ns. Energy Cuts are applied"
	descrecoenergy = "RECO Energy in GeV"
	descrecotimeen = "Timing in ns(y) vs Energy in GeV(x). Cuts on Energy are applied"
	desctpet = "Trigger Primitives Et"
	desctpetcorr = "TP Et Correlation. Data(y) vs Emulator(x)"
	descrawsum = "RAW Summary vs LS"
	descdigisum = "DIGI Summary vs LS"
	desctpsum = "TP Summary vs LS"
	descrecosum = "RECO Summary vs LS"

	#	define the list for copying
	listToCopy = []
	listToCopy[len(listToCopy):] = [
		#	Timing
		["Timing", "DigiTask", "/SubDetPM_iphi", descdigitiming],
		["Timing", "DigiTask", "/vsLS_SubDetPM_iphi", descdigitiming],
		["Timing", "DigiTask", "/vsieta_SubDet_iphi", descdigitiming],
		["Timing", "DigiTask", "/vsiphi_SubDet_ieta", descdigitiming],
		["Timing", "RecHitTask", "/SubDetPM_iphi", descrecotiming],
		["Timing", "RecHitTask", "/vsLS_SubDetPM_iphi", descrecotiming],
		["Timing", "RecHitTask", "/vsLS_SubDetPM_iphi", descrecotiming],
		["Timing", "RecHitTask", "/vsiphi_SubDet_ieta", descrecotiming],
		["Timing", "RecHitTask", "/vsieta_SubDet_iphi", descrecotiming],

		#	Energy
		["Energy", "RecHitTask", "/SubDetPM_iphi", descrecoenergy],

		#	Timing vs Energy
		["TimingvsEnergy", "RecHitTask", "/SubDetPM_iphi", descrecotimeen],

		#	Et
		["Et", "TPTask", "/SubDetPM_iphi", desctpet],
		["EtCorrelation", "TPTask", "/SubDetPM_iphi", desctpetcorr],

		#	Summary
		["Summary", "RawTask", "/vsLS", descrawsum],
		["Summary", "DigiTask", "/vsLS", descdigisum],
		["Summary", "TPTask", "/vsLS", desctpsum],
		["Summary", "RecHitTask", "/vsLS", descrecosum],
	]

	#	generate layouts
	parser = Parser.Parser(rootFileName)
	objs = parser.traverse()
	for path in objs.keys():
		counter = 0;
		for x in listToCopy:
			if x[0] in path:
				if x[1] in path and x[2] in path:
					print path
					desc = x[3]
					for obj in objs[path]:
						lname = "%s%s/%s/%s" % (x[0], 
							x[2], dictTasks[x[1]], obj.GetName())
						pathname = path+"/"+obj.GetName()
						create_singlelayout(pyOutFile, lname, 
							"Hcal"+pathname, desc)
			counter+=1

#		if "Timing" in path:
#			if "DigiTask" in path and "/SubDetPM_iphi" in path:
#				print path
#				desc = "Nominal fC weighted Time Average. Cuts on the amplitude are applied."
#				for obj in objs[path]:
#					lname = nameBase + "SubDetPM_iphi/DIGI/" + obj.GetName()
#					pathname = path+"/"+obj.GetName()
#					create_singlelayout(pyOutFile, lname, "Hcal"+pathname, desc)
#			if "RecHitTask" in path and "/SubDetPM_iphi" in path:
#				print path
#				desc = "RECO Timing in ns. Energy Cuts are applied"
#				for obj in objs[path]:
#					lname = nameBase + "SubDetPM_iphi/RECO/" + obj.GetName()
#					pahtname = path+"/"+obj.GetName()
#					create_singlelayout(pyOutFile, lname, "Hcal"+pathname, desc)

if __name__=="__main__":
	print "Generating..."
	
	output = open(sys.argv[1], "w")
	inpRoot = sys.argv[2]
	inpTxt = sys.argv[3]
	create_fromTxt(output, inpTxt)
	create_fromROOT(output, inpRoot)


