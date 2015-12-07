"""
file:		Comparator.py
author:		Viktor Khristenko

description:

"""

import runInfo, ROOT
from utilities import getRunNumber

class ComparisonSet:
	""" Single Quantity Comparison Set """
	def __init__(self, qname):
		self.qname = qname
		self.hmr = ROOT.TH1D(qname+"_MeansRatios", qname + " Means Ratios",
			100, 0.5, 1.5)
		self.hmd = ROOT.TH1D(qname+"_MeansDifferences", 
			qname + " Means Differences", 100, -0.5, 0.5)
		self.hrr = ROOT.TH1D(qname+"_RMSsRatios", qname + " RMSs Ratios",
			100, 0.5, 1.5)
		self.hrd = ROOT.TH1D(qname+"_RMSsDifferences", 
			qname + " RMSs Differences", 100, -0.5, 0.5)

	def compare(self, emap, hsett, hsetr):
		pass

class HistogramSet:
	""" A set of histograms that should be compared to the reference """
	def __init__(self, qname):
		self.qname = qname
		if qname!="Pedestal":
			ROOT.gDirectory.cd("2D/" + qname)
		self.hmd1 = ROOT.gDirectory.Get(qname+"Means_Depth1")
		self.hmd2 = ROOT.gDirectory.Get(qname+"Means_Depth2")
		self.hmd3 = ROOT.gDirectory.Get(qname+"Means_Depth3")
		self.hmd4 = ROOT.gDirectory.Get(qname+"Means_Depth4")
		self.hrd1 = ROOT.gDirectory.Get(qname+"RMSs_Depth1")
		self.hrd2 = ROOT.gDirectory.Get(qname+"RMSs_Depth2")
		self.hrd3 = ROOT.gDirectory.Get(qname+"RMSs_Depth3")
		self.hrd4 = ROOT.gDirectory.Get(qname+"RMSs_Depth4")

		#	exit back to the folder
		ROOT.gDirectory.cd("..")
		
def generate(files, info):
	""" trigger the comparison """

	#	initialization
	tfile = files[0]
	rfiles = files[1:]
	rtfile = TFile(tfile, "update")

	#	iterate over each reference file and add the comparison
	for f in rfiles:
		#	1. create a dir "Comparison_<refrun>" folder in the appropriate task
		#	2. For each quantity to be compared, generate a folder with 
		#		comparison histograms
		#		for pedestal it is only Pedestal
		#		for led/laser it is either Signal or Time
		refRunNumber = getRunNumber(f)
		rfile = TFile(f)
		if info.runType=="Pedestal":
			#	setup reference histos
			rfile.cd("DQMData/Run %s/Hcal/Run summary/PedestalTask" % 
				refRunNumber)
			hsetr = HistogramSet("Pedestal")

			#	setup target histos
			rtfile.cd("DQMData/Run %s/Hcal/Run summary/PedestalTask" % 
				info.runNumber)
			hsett = HistogramSet("Pedestal")

			#	setup comparison set
			ROOT.gDirectory.mkdir("Comparison_%d" % refRunNumber)
			ROOT.gDirectory.cd("Comparison_%d" % refRunNumber)
			pset = ComparisonSet("Pedestal")
			
			#	compare and save
			pset.compare(hsett, hsetr)
			rtfile.Write()
		elif info.runType=="LED":
			#	setup reference histos
			rfile.cd("DQMData/Run %s/Hcal/Run summary/LEDTask" % 
				refRunNumber)
			hsetrS = HistogramSet("Signal")
			hsetrT = HistogramSet("Timing")

			#	setup target histos
			rtfile.cd("DQMData/Run %s/Hcal/Run summary/LEDTask" % 
				info.runNumber)
			hsettS = HistogramSet("Signal")
			hsettT = HistogramSet("Timing")

			#	setup comparison set
			ROOT.gDirectory.mkdir("Comparison_%d" % refRunNumber)
			ROOT.gDirectory.cd("Comparison_%d" % refRunNumber)
			psetS = ComparisonSet("Signal")
			psetT = ComparisonSet("Timing")
			
			#compare and save
			psetS.compare(hsettS, hsetrS)
			psetT.compare(hsettT, hsetrT)
			rtfile.Write()
		elif info.runType=="Laser":
			#	setup reference histos
			rfile.cd("DQMData/Run %s/Hcal/Run summary/LaserTask" % 
				refRunNumber)
			hsetrS = HistogramSet("Signal")
			hsetrT = HistogramSet("Timing")

			#	setup target histos + init comparison set
			rtfile.cd("DQMData/Run %s/Hcal/Run summary/LaserTask" % 
				info.runNumber)
			hsettS = HistogramSet("Signal")
			hsettT = HistogramSet("Timing")

			#	setup comparsion set
			ROOT.gDirectory.mkdir("Comparison_%d" % refRunNumber)
			ROOT.gDirectory.cd("Comparison_%d" % refRunNumber)
			psetS = ComparisonSet("Signal")
			psetT = ComparisonSet("Timing")

			#	compare and save
			psetS.compare(hsettS, hsetrS)
			psetT.compare(hsettT, hsetrT)
			rtfile.Write()
		else:
			continue

if __name__=="__main__":
	generate()




