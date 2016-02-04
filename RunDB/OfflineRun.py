
#
#	Offline Run
#

from Run import Run

class OfflineRun(Run):
	def __init__(self, run, nevents, timestamp, dataset):
		Run.__init__(self, run, nevents, timestamp)
		self.__dataset = dataset

	def dataset(self):
		return self.__dataset

	def processingType(self):
		return "Offline"

if __name__=="_main__":
	print "OfflineRun hello"

