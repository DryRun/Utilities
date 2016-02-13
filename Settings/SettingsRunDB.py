"""
Settings for the Run DataBase. Constant as is - are not imported
"""

dbname = "RunDB"

processingTypes = ["online-central", "offline-central", "local",
	"online-playback", "Offline-playback"]
onlineStreams = ["physics", "calib"]
configurations = [
	"pedestal", "led", "raddam", "laserhbm", "laserhbp", "laserhem",
	"laserhep", "laserho", "laserhf"
]
offlineDatasets = ["MINIBIAS", "COMMISSIONING", "COSMICS",
	"BTAG"]

lvl2 = [onlineStreams, offlineDatasets, configurations,
	onlineStreams, offlineDatasets]

structure = {processingTypes[x]:lvl2[x] for x in range(len(lvl2))}


