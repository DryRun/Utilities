"""
Settings for the Run DataBase. Constant as is - are not imported
"""

dbname = "RunDB"

processingTypes = ["online-central", "offline-central", "local",
	"online-playback", "Offline-playback"]
onlineStreams = ["physics", "calib"]
configurations = [
	"pedestal", "led", "raddam", "laserhbm", "laserhbp", "laserhem",
	"laserhep", "laserho", "laserhf", "laserhpd"
]
offlineDatasets = ["MINIBIAS", "COMMISSIONING", "COSMICS",
	"BTAG"]

lvl2 = [onlineStreams, offlineDatasets, configurations,
	onlineStreams, offlineDatasets]

structure = {}
for i in range(len(lvl2)):
	structure[processingTypes[i]]=lvl2[i]

#	below is not compatible with python 2.6.6 and earlier
#structure = {processingTypes[i]:lvl2[i] for i in range(len(lvl2))}


