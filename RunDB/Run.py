
#
#	Run Class. Base class for all run types
#

class Run:
	"""
	Run Class. timestamp is a string of YYYY:MM:DD
	"""
	def __init__(self, run, nevents, timestamp):
		self.__run = run
		self.__nevents = nevents
		self.__timestamp = timestamp
		self.__comment = "None"
		self.__state = -1

	def run(self):
		return str(self.__run)

	def nevents(self):
		return self.__nevents

	def processingType(self):
		return "Run"

	def timestamp(self):
		return self.__timestamp

	def comment(self, s):
		self.__comment = s

	def comment(self):
		return self.__comment

	def state(self):
		return self.__state

	def changeState(self, state):
		self__state = state

if __name__=="__main__":
	print "Hello"
	r = Run(1, 10, "2015:1:1")
	print r.run()
	print r.nevents()

