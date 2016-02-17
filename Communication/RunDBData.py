"""
Run DB Data - defines Run DB Server Specific Data format to be exchanged
"""

class RunDBData:
	def __init__(self, data=None):
		if data!=None:
			self.data = data
	
	def unpackQuery(self):
		self.qn = self.data[0]
		self.branch = self.data[1]




