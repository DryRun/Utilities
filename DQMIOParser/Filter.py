#!/usr/bin/python

#
#	ROOT DQM TH1-like Filter
#

import sys
import ROOT as R

utilDir = "/Users/vk/software/HCALDQM/Utilities/Utils"
sys.path[len(sys.path):] = [utilDir]
import utilities as util

#	define the Filter class
class Filter:
	"""
		Filter Class
	"""
	def __init__(self, **argv):
		self.quantity = argv["quantity"]
		self.hasher = argv["hasher"]
		self.taskName = argv[taskName]

	def filter(self, objs):
		r = {}
		for path in objs.keys():
			if self.quantity in path and self.taskName in path and \


