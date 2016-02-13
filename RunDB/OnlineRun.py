
from Run import Run

class OnlineRun(Run):
	def __init__(self, run, nevents, timestamp, stream):
		Run.__init__(self, run, nevents, timestamp)
		self.__stream = stream

	def stream(self):
		return self.__stream

	def processingType(self):
		return "online"

	def resolve(self):
		return (self.stream(), self.run())

if __name__=="__main__":
	print "OnlineRun Hello"

	onr = OnlineRun(1, 10, "2016:1:1", "Physics")
	print onr.stream()
	print onr.comment()
























