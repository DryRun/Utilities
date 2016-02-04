
#
#	Defines the DB Structure here
#	to be imported
#

runDBNameBase = "RunDB"
processingTypes = ["Online", "Offline", "Local"]
runDBNames = [runDBNameBase+x for x in processingTypes]
streams = ["Physics", "Calib"]
configurations = ["PEDESTAL", "LED", "RADDAM", "LASERHBM",
	"LASERHBP", "LASERHEM", "LASERHEP", "LASERHO", "LASERHF"]
datasets = ["ALCALUMIPIXELS", "MINIBIAS",
	"BJETPLUSX", "BJETPLUSX25ns", "BTAG",
	"CHARMONIUM", "COMMISSIONING", "COSMICS"]

structure = {
	processingTypes[0]:streams,
	processingTypes[1]:datasets,
	processingTypes[2]:configurations
}

if __name__=="__main__":
	print runDBNameBase
	print runDBNames
	print processingTypes
	print streams
	print configurations
	print datasets
	print structure
