
#
#	Local Run Class 
#

import Run

class LocalRun(Run.Run):
	def __init__(self, run, nevents, timestamp, config):
		Run.Run.__init__(self, run, nevents, timestamp)
		self.__config = config

	def configuration(self):
		return self.__config

	def processingType(self):
		return "local"

	def resolve(self):
		return (self.configuration(), self.run())

if __name__=="__main__":
	print "LocalRun Hello"

	lr = LocalRun(1, 10, "2016:1:1", "Pedestal")
	print lr.timestamp()
	print lr.configuration()
	print lr.processingType()
	print lr.__name__


