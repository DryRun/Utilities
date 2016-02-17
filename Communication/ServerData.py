"""
ServerData - all the interaction with data format transferred thru the wire.
Pickling, unpicling....
"""

import pickle

class ServerData:
	def __init__(self, pickleddata=None):
		if pickleddata!=None:
			self.lcmds = pickle.loads(pickleddata)
		else:
			self.lcmds = []

	def unpackPacket(self):
		return (self.lcmds[0], self.lcmds[1])

	def buildPacket(self, cmd, sdata):
		return pickle.dumps([cmd, sdata])
	




