"""
Base Class for Masters/Servers/Clients/Executors....
"""

class XXX:
	def __init__(self, lid):
		self.lid = lid #	local id, within a process

	def initialize(self):pass

	def start(self):pass

	def work(self):pass

	def work(self, cmddata):pass

	def finialize(self):pass
