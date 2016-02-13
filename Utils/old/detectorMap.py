"""
file:			detectorMap.py
author:			Viktor Khristenko
"""

import sys

#
#	Id Classes
#
class Id:
	def __init__(self, uid):
		self.uid = uid

class DetId(Id):
	def __init__(self, uid, subdet, iphi, ieta, depth):
		self.uid = uid
		self.subdet = subdet
		self.iphi = iphi
		self.ieta = ieta
		self.depth = depth

	def display(self):
		print "did: %d %s %d %d %d" % (self.uid, self.subdet, self.iphi,
			self.ieta, self.depth)
	
class ElectronicsId(Id):
	def __init__(self, uid, crate, slot, tb, dcc, spigot, fiber, fiberch):
		self.uid = uid
		self.crate = crate
		self.slot = slot
		self.tb = tb
		self.dcc = dcc
		self.spigot = spigot
		self.fiber = fiber
		self.fiberch = fiberch

	def display(self):
		print "eid: %d %d %d %c %d %d %d %d" % (self.uid,
			self.crate, self.slot, self.tb, self.dcc, self.spigot, self.fiber,
			self.fiberch)

class FullId(Id):
	def __init__(self, did, eid):
		self.uid = did.uid
		self.did = did
		self.eid = eid
	
	def display(self):
		print "##############################"
		self.did.display()
		self.eid.display()

class Map:
	def __init__(self, txt):
		self.txt = txt
		f = open(self.txt)
		uid = 0
		self.ids = []
		for line in f:
			#	skip if a comment
			if line[0]=="#":
				continue

			v = line.split()
			eid = ElectronicsId(uid, int(v[1]), int(v[2]), v[3], int(v[4]), 
				int(v[5]), int(v[6]), int(v[7]))
			did = DetId(uid, v[8], int(v[10]), int(v[9]), int(v[11]))
			fid = FullId(did, eid)
			self.ids[len(self.ids):] = [fid]

			#	increment uid
			uid+=1

	def display(self):
		for x in self.ids:
			x.display()

#
#	Main
#
def main():
	""" Main Entry Point """
	txt = sys.argv[1]
	emap = Map(txt)
	emap.display()

if __name__=="__main__":
	main()













