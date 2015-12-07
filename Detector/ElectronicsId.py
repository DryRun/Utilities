#!/usr/bin/python

#
#	HCAL ElectronicsId Class
#

from Id import Id
from Constants import *

class ElectronicsId(Id):
	"""
	"""
	def __init__(self, **d):
		"""
		"""
		self.type = d["type"]
		self.crate = d["crate"]
		self.fiber = d["fiber"]
		self.fiberCh = d["fiberCh"]
		if self.type=="uTCA":
			self.slot = d["slot"]
		else:
			self.dcc = d["dcc"]
			self.spigot = d["spigot"]
			self.tb = d["tb"]

		#
		Id.__init__(self, self.myhash())
		if self.type=="uTCA":
			self.repr = "<uTCA ElectronicsId id=%d crate=%d slot=%d fiber=%d fiberCh=%d>" % (self.id, self.crate, self.slot, self.fiber, self.fiberCh)
		else:
			self.repr = "<VME ElectronicsId id=%d crate=%d tb=%s dcc=%d spigot=%d fiber=%d fiberCh=%d>" % (self.id, self.crate, self.tb, self.dcc, self.spigot,
				self.fiber, self.fiberCh)

	def myhash(self):
		if self.type=="uTCA":
			icrate = self.crate-1
			islot = self.slot-1
			ifiber = self.fiber-1
			ifiberch = self.fiberCh
			
			h = ( icrate*SLOTS_uTCA_NUM*FIBERS_uTCA_NUM*FIBERCHS_NUM  + 
				islot*FIBERS_uTCA_NUM*FIBERCHS_NUM + 
				ifiber*FIBERCHS_NUM + ifiberch
			)
			return h
		else:
			icrate = self.crate
			ispigot = self.spigot
			ifiber = self.fiber-1
			ifiberch = self.fiberCh

			h = ( icrate*SPIGOTS_VME_NUM*FIBERS_VME_NUM*FIBERCHS_NUM + 
				ispigot*FIBERS_VME_NUM*FIBERCHS_NUM + 
				ifiber*FIBERCHS_NUM + ifiberch
			)
			return h

if __name__=="__main__":
	eid1 = ElectronicsId(type="uTCA", crate=22, slot=5, fiber=3, fiberCh=0)
	eid2 = ElectronicsId(type="uTCA", crate=22, slot=5, fiber=5, fiberCh=0)
	print(eid1)
	print(eid2)


