#!/usr/bin/python

#
#	ROOT DQM File Parser Class
#	Returns 
#

import sys
import ROOT as R

#	to import utilities modules
utilDir = "/Users/vk/software/HCALDQM/Utilities/Utils"
sys.path[len(sys.path):] = [utilDir]
import utilities as util

#	define the Parser class
class Parser:
	"""
		Parser Class. Parses a root file of the DQM type and returns
		all the TH1-derivable objects as a dictionary.
	"""
	def __init__(self, rootFileName):
		"""
		Get the Run Number. Open the file and cd to the Run Summary Directory
		Initialize whatever is needed
		"""

		self.__rootFileName = rootFileName
		self.__runNumber = util.getRunNumber(rootFileName)
		self.__rootFile = R.TFile(self.__rootFileName)
		self.__rsDir = self.__rootFile.GetDirectory(
			"DQMData/Run %d/Hcal/Run summary/" % self.__runNumber)
		pass
	
	def traverse(self):
		"""
		Traverse the ROOT Folder Tree
		"""

		#	get into the Run Summary Directory
		#	each Task Folder is sitting there
		objDict = {}
		for dirKey in self.__rsDir.GetListOfKeys():
			dirName = dirKey.GetName()
			#	launch the traversing of each task directory
			self.traverseDir(self.__rsDir.GetDirectory(dirName), objDict)
		
		return objDict

	def traverseDir(self, cDir, objDict, topPath=""):
		"""
		TopPath - path to the current Directory not including it
		"""
		for key in cDir.GetListOfKeys():
			obj = key.ReadObj()
			#	if it is a folder, traverse recursively
			if obj.InheritsFrom("TDirectoryFile"):
				self.traverseDir(obj, objDict, 
					topPath=topPath+"/"+cDir.GetName())
			else:
				path = topPath+"/"+cDir.GetName()
				if path in objDict.keys():
					objDict[path][len(objDict[path]):] = [obj]
				else:
					objDict[path] = [obj]

if __name__=="__main__":
	print "Hello"
	fileName = "/Users/vk/research/tmptmp/DQM_V0001_Hcal_R000262548.root"
	parser = Parser(fileName)
	d = parser.traverse()
	print d

