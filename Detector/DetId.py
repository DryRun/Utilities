#!/usr/bin/python

#
#	HCAL DetId Class
#

from Id import Id
from Constants import *

class DetId(Id):
	"""
	"""
	def __init__(self, **d):
		"""
		"""
		self.iphi = d["iphi"]
		self.ieta = d["ieta"]
		self.depth = d["depth"]
		self.subdetName = d["subdetName"]
		self.subdet = SUBDET_NAME.index(self.subdetName)
		
		#	set the id as the hash and declare the representation
		Id.__init__(self, self.myhash())
		self.repr = "<DetId id=%d subdet=%s iphi=%d ieta=%d depth=%d>" % (
			self.id, self.subdetName, self.iphi, self.ieta, self.depth)

	def myhash(self):
		iiphi = self.iphi-1
		if self.ieta==-29:
			if self.subdetName=="HE":
				iieta = abs(self.ieta)-1
			elif self.subdetName=="HF":
				iieta = abs(self.ieta)
		elif self.ieta==29:
			if self.subdetName=="HE":
				iieta = IETA_NUM + self.ieta-1
			elif self.subdetName=="HF":
				iieta = IETA_NUM + self.ieta
		elif self.ieta>0:
			iieta = self.ieta - 1 + IETA_NUM
		else:
			iieta = abs(self.ieta) - 1

		idepth = self.depth-1
		isubdet = self.subdet

		h = (isubdet*IPHI_NUM*2*IETA_NUM*DEPTH_NUM + 
			iiphi*2*IETA_NUM*DEPTH_NUM + 
			iieta*DEPTH_NUM + idepth
		)

		return h

	
#	testing
if __name__=="__main__":
	did1 = DetId(iphi=1, subdetName="HB", ieta=-10, depth=1)
	did2 = DetId(ieta = -2, depth=1, subdetName="HB", iphi=1)
	print(did1)
	print(did2)
