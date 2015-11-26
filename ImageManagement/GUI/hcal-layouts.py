
#	HCAL DQM Layouts for Main Application
#


if __name__=="__main__":
	class DQMItem:
		def __init__(self, layout):
			print layout

	dqmitems = {}

def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

#	Summary Layout
hcallayout(dqmitems, "01 HCAL Summary",
	[
		{
			"path" : "Hcal/RawTask/Summary/Summary",
			"description" : "HCAL RAW Format Summary per FED"
		},
		{
			"path" : "Hcal/RecHitTask/Summary/Summary",
			"description" : "HCAL REC HIT Format Summary per SubDetetor"
		}
	],
	[
		{
			"path" : "Hcal/DigiTask/Summary/Summary",
			"description" : "HCAL DIGI Format Summary per SubDetetor"
		},
		{
			"path" : "Hcal/TPTask/Summary/Summary",
			"description" : "HCAL Trigger Primitive Format Summary per SubDetetor"
		}
	]
)

#	Digi Layouts
hcallayout(dqmitems, "02 HCAL DIGI Occupancy vs LS",
	[
		{
			"path" : "HcalDigiTask/Occupancy/"
		}
	]
)

