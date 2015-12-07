#!/usr/bin/python

#
#	A simple Hcal emap parser
#

import sys

coreDir = "/Users/vk/software/HCALDQM/Utilities/Detector"
sys.path[len(sys.path):] = [coreDir]
from Constants import *
from DetId import DetId
from ElectronicsId import ElectronicsId

def parse(fileName):
	"""
	"""
	f = open(fileName)
	e2d = {}; d2e = {}
	for line in f:
		if line[0]=="#":
			continue
		v = line.split()

		# emap format is hard coded
		crate = int(v[1])
		slot = int(v[2])
		tb = v[3]
		dcc = int(v[4])
		spigot = int(v[5])
		fiber = int(v[6])
		fiberCh = int(v[7])
		subdet = v[8]
		ieta = int(v[9])
		iphi = int(v[10])
		depth = int(v[11])

		if not (subdet=="HB" or subdet=="HE" or subdet=="HO" or subdet=="HF"):
			continue

		if tb=="t" or tb=="b":
			t = "VME"
		else:
			t = "uTCA"

		did = DetId(subdetName=subdet, iphi=iphi, ieta=ieta, depth=depth)
		if t=="VME":
			eid = ElectronicsId(type=t, crate=crate, fiber=fiber,
				fiberCh=fiberCh, dcc=dcc, tb=tb, spigot=spigot)
		else:
			eid = ElectronicsId(type=t, crate=crate, slot=slot, fiber=fiber,
				fiberCh=fiberCh)

		e2d[eid] = did
		d2e[did] = eid
	return [e2d, d2e]

if __name__=="__main__":
	l = parse(sys.argv[1])
	e2d = l[0]
	d2e = l[1]

	print "Electronics to Detector Map"
	for x in e2d:
		print x, e2d[x]
	print "Detector to Electronics Map"
	for x in d2e:
		print x, d2e[x]
