"""
Run DB Data - defines Run DB Server Specific Data format to be exchanged
"""

import pickle

#	query defs
query_checkIfExists = 0
query_addRun = 1
query_deleteRun = 2
query_updateRun = 3
query_list = 4
query_number = 5

class RunDBData:
	""" knows how to unpack query data """
	def __init__(self, data=None):
		if data!=None:
			self.data = data
	
	def unpackQuery(self):
		""" 
		The format of the msg is:
		0 - query number as defined above
		1 - branch or processing type
		2 - runobj
		"""
		qid = int(self.data[0])
		ptype = self.data[1]
		runobj = self.data[2]
		return (qid, ptype, runobj)

	def packResult(self, qid, result):
		"""
		The format of the result msg:
		0 - qid
		1 - whatever the result is depending on the initial query
		"""
		return pickle.dumps([qid, result])

	def unpackResult(self, rtmsg):
		return pickle.loads(rtmsg)
