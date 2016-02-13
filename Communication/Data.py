"""
Data - all the interaction with data format transferred thru the wire.
Pickling, unpicling....
"""

import pickle

class Data:
	def __init__(self, pickleddata):
		self.lcmds = pickle.loads(pickleddata)

	def getscmd(self):
		return self.lcmds[0]

	def getsdata(self):
		return self.lcmds[1]
	




