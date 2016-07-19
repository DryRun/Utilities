#!/usr/bin/python

import sys,os, re
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import DQMIO.Parser as Parser
from layout import Layout, Plot
from Monitorables import variables, analysis_tasks, allgroups
from Common import *

def relink(subsystem, layoutbase, objs, out, agroups, detail):
	for path in objs.keys():
		print subsystem+path
		r = match_path(path)
		groups = r.groups()
		task = groups[0]
		if task not in analysis_tasks.keys() or len(groups)<2:
			#	if not one of my tasks or if it's a xml object
			continue
		module = analysis_tasks[task]
		var = groups[1]
		if var not in variables[module].keys():
			#	if this variable is not in the list of monitorables
			#	for this task continue
			print "Missing Monitorable for path %s" % path
			continue

		#	first relink all the MEs
		if len(groups)==2:
			#	if it's a single ME
			for i in range(len(objs[path])):
				name = objs[path][i].GetName()
				p = Plot(subsystem+path+"/%s" % name, 
					variables[module][var])
				newpath = "%s/%s" % (var, module)
				l = Layout(newpath, layoutbase, [[p]])
				if detail:out.write("\n%s\n" % l)
	
				#	grouping
				for g in agroups:
					info = {"task" : module,
							"var" : var, "hasher" : "NOHASHER"}
					nskipped=0; nms = 0;
					""" 
					grouping is based on 2 things:
					1 - variable name
					2 - task name
					"""
					for key in g.tokens.keys():
						if g.tokens[key]==0:
							nskipped+=1
						elif g.tokens[key]==info[key]:
							nms+=1
					if nms+nskipped==len(g.tokens.keys()):
						g.add(p)
		else:
			hasher = groups[2]
			for o in objs[path]:
				p = Plot(subsystem+path+"/%s" % o.GetName(), 
					variables[module][var])
				newpath = "%s/%s/%s/%s" % (
					var, module, hasher, o.GetName())
				l = Layout(newpath, layoutbase, [[p]])
				if detail:out.write("\n%s\n" % l)

				#	grouping
				for g in agroups:
					info = {"task" : module,
						"var" : var, "hasher" : hasher}
					nskipped=0; nms = 0;
					""" 
					grouping is based on 2 things:
					1 - variable name
					2 - task name
					3 - hasher
					"""
					for key in g.tokens.keys():
						if g.tokens[key]==0:
							nskipped+=1
						elif g.tokens[key]==info[key]:
							nms+=1
					if nms+nskipped==len(g.tokens.keys()):
						g.add(p)


def group(layoutbase, out, detail, groups):
	print "### Generating Groups!"
	skipList = []
	for g in groups:
		#	this is for uniting groups or skipping the empty groups
		if g in skipList or g.empty():
			continue
		for g2 in groups:
			if g2 is not g and g.name==g2.name:
				g.l.extend(g2.l)
				skipList.append(g2)
		#	create a layout out of a group...
		if not g.include(detail): continue
		l = Layout(g.name, layoutbase, g.dump())
		print g.name
		out.write("\n%s\n" % l)

def main(argv):
	"""
	input:
	1 - csv file list 
	2 - output file name
	3 - for physics [0] or calibration [1] - which workflow 
	4 - verbosity level - for shifters[False] or for hcal[True]?
	"""
	print "Starting Layout Generation..."
	csv_filelist = argv[0]
	outname = argv[1]
	physcalib = int(argv[2]) 
	forshifters = int(argv[3])
	layoutbase = argv[4]
	out = open(outname, "w")
	out.write(
"""if __name__=="__main__":
	class DQMItem:
		def __init__(self,layout):
			print layout
	dqmitems={}""")
	out.write("\n\n")
	users = "Hcal"
	if forshifters==0:
		users="00 Shift"
		if physcalib>0:
			mainsubsystem = "HcalCalib"
		else:
			mainsubsystem = "Hcal"
	elif physcalib>0:
		users="HcalCalib"
		mainsubsystem = "Layouts"
	else:
		users="Hcal"
		mainsubsystem="Layouts"
	out.write("def %s(i, p, *rows): i['%s/%s/' + p] = DQMItem(layout=rows)\n\n" % (layoutbase, users, mainsubsystem)) 

	#	parse all the histograms
	filelist = csv_filelist.split(",")
	objs = {}
	for f in filelist:
		i = f.find("DQM_V")
		filename = f[i:len(f)]
		subsystem = match_filename(filename, "Online").groups()[1]
		subsystem = subsystem[1:len(subsystem)]
		print "Will parse ROOT file: %s, subsystem %s" % (filename, subsystem)
		parser = Parser.Parser(f, subsystem)
		os = parser.traverse()
		relink(subsystem, layoutbase, os, out,allgroups[physcalib],forshifters)
		objs.update(os)
	group(layoutbase, out, forshifters, allgroups[physcalib])
	
	# close the output file
	out.close()

if __name__=="__main__":
	main(sys.argv[1:])
