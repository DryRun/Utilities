#
#	HCAL DQM Layouts
#

if __name__=='__main__':
	class DQMItems:
		def __init__(self, layout):
			print layout
	dqmitems = {}

def hcallayout(i, p, *rows):
	i['Hcal/Layouts/' + p] = DQMItem(layout=rows)

hcallayout(dqmitems, '01 HCAL RAW/DIGI/TP/RECHIT Summary
', [{'path' : 'RawTask/Summary/Summary', 'description' : 'Hcal/HCAL RAW Format Summary per FED'},{'path' : 'RecHitTask/Summary/Summary', 'description' : 'Hcal/HCAL REC HIT Format Summary per SubDetetor'}],[{'path' : 'DigiTask/Summary/Summary', 'description' : 'Hcal/HCAL DIGI Format Summary per SubDetetor'},{'path' : 'TPTask/Summary/Summary', 'description' : 'Hcal/HCAL Trigger Primitive Format Summary per SubDetetor'}])

hcallayout(dqmitems, '02 HCAL DIGI Occupancy vs LS
', [{'path' : 'HcalDigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HB', 'description' : 'Hcal/HB Occupancy vs LS'},{'path' : 'HcalDigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HE', 'description' : 'Hcal/HE Occupancy vs LS'}],[{'path' : 'HcalDigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HF', 'description' : 'Hcal/HF Occupancy vs LS'},{'path' : 'HcalDigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HO', 'description' : 'Hcal/HO Occupancy vs LS'}])

hcallayout(dqmitems, '03 HCAL DIGI Occupancy 2D
', [{'path' : 'HcalDigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth1', 'description' : 'Hcal/Depth 1 Occupancy.'},{'path' : 'HcalDigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth2', 'description' : 'Hcal/Depth 2 Occupancy.'}],[{'path' : 'HcalDigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth3', 'description' : 'Hcal/Depth 3 Occupancy.'},{'path' : 'HcalDigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth4', 'description' : 'Hcal/Depth 4 Occupancy.'}])

hcallayout(dqmitems, '04 HCAL DIGI Missing Channels per 1LS
', [{'path' : 'HcalDigiTask/Missing/1LS_depth/Missing_Depth1', 'description' : 'Hcal/Depth 1 Missing channels per 1LS. Updated each 10LS'},{'path' : 'HcalDigiTask/Missing/1LS_depth/Missing_Depth2', 'description' : 'Hcal/Depth 2 Missing channels per 1LS. Updated each 10LS'}],[{'path' : 'HcalDigiTask/Missing/1LS_depth/Missing_Depth3', 'description' : 'Hcal/Depth 3 Missing channels per 1LS. Updated each 10LS'},{'path' : 'HcalDigiTask/Missing/1LS_depth/Missing_Depth4', 'description' : 'Hcal/Depth 4 Missing channels per 1LS. Updated each 10LS'}])

hcallayout(dqmitems, '05 HCAL DIGI Missing Channels per 1LS vs LS
', [{'path' : 'HcalDigiTask/Missing/1LSvsLS_SubDet/Missing_HB', 'description' : 'Hcal/Number of HB missing channels per 1LS.'},{'path' : 'HcalDigiTask/Missing/1LSvsLS_SubDet/Missing_HE', 'description' : 'Hcal/Number of HE missing channels per 1LS.'}],[{'path' : 'HcalDigiTask/Missing/1LSvsLS_SubDet/Missing_HF', 'description' : 'Hcal/Number of HF missing channels per 1LS.'},{'path' : 'HcalDigiTask/Missing/1LSvsLS_SubDet/Missing_HO', 'description' : 'Hcal/Number of HO missing channels per 1LS.'}])

hcallayout(dqmitems, '06 HCAL RECHIT Timing 2D
', [{'path' : 'HcalRecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth1', 'description' : 'Hcal/Depth 1 Timing.'},{'path' : 'HcalRecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth2', 'description' : 'Hcal/Depth 2 Timing.'}],[{'path' : 'HcalRecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth3', 'description' : 'Hcal/Depth 3 Timing.'},{'path' : 'HcalRecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth4', 'description' : 'Hcal/Depth 4 Timing.'}])

hcallayout(dqmitems, '07 HCAL RECHIT HBHEabc Timing
', [{'path' : 'HcalRecHitTask/Timing/HBHEPartition_EHBHE5HO5HF5/Timing_HBHEa', 'description' : 'Hcal/HBHEa Timing'},{'path' : 'HcalRecHitTask/Timing/HBHEPartition_EHBHE5HO5HF5/Timing_HBHEb', 'description' : 'Hcal/HBHEb Timing'},{'path' : 'HcalRecHitTask/Timing/HBHEPartition_EHBHE5HO5HF5/Timing_HBHEc', 'description' : 'Hcal/HBHEc Timing'}])

hcallayout(dqmitems, '08 HCAL RECHIT Energy 2D
', [{'path' : 'HcalRecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth1', 'description' : 'Hcal/Depth 1 Energy'},{'path' : 'HcalRecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth2', 'description' : 'Hcal/Depth 2 Energy'}],[{'path' : 'HcalRecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth3', 'description' : 'Hcal/Depth 3 Energy'},{'path' : 'HcalRecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth4', 'description' : 'Hcal/Depth 4 Energy'}])

hcallayout(dqmitems, '09 HCAL RECHIT Energy per SubDetector
', [{'path' : 'HcalRecHitTask/Energy/SubDet/Energy_HB', 'description' : 'Hcal/Energy HB'},{'path' : 'HcalRecHitTask/Energy/SubDet/Energy_HE', 'description' : 'Hcal/Energy HE'}],[{'path' : 'HcalRecHitTask/Energy/SubDet/Energy_HF', 'description' : 'Hcal/Energy HF'},{'path' : 'HcalRecHitTask/Energy/SubDet/Energy_HO', 'description' : 'Hcal/Energy HO'}])

hcallayout(dqmitems, '10 HCAL TP Occupancy vs LS
', [{'path' : 'HcalTPTask/Occupancy/DatavsLS_TPSubDet/Occupancy_Data_HBHE', 'description' : 'Hcal/HBHE Data TPs Occupancy vs LS'},{'path' : 'HcalTPTask/Occupancy/DatavsLS_TPSubDet/Occupancy_Data_HF', 'description' : 'Hcal/HF Data TPs Occupancy vs LS'}],[{'path' : 'HcalTPTask/Occupancy/DatavsLS_TPSubDet/Occupancy_Emul_HBHE', 'description' : 'Hcal/HBHE Emulator TPs Occupancy vs LS'},{'path' : 'HcalTPTask/Occupancy/DatavsLS_TPSubDet/Occupancy_Emul_HF', 'description' : 'Hcal/HF Emulator TPs Occupancy vs LS'}])

hcallayout(dqmitems, '11 HCAL TP Occupancy 2D
', [{'path' : 'HcalTPTask/Occupancy/Occupancy_Data', 'description' : 'Hcal/Data Occupancy'},{'path' : 'HcalTPTask/Occupancy/Occupancy_Emul', 'description' : 'Hcal/Emulator Occupancy'}])

hcallayout(dqmitems, '12 HCAL TP Et Correlation vs LS
', [{'path' : 'HcalTPTask/Et/CorrRatiovsLS_TPSubDet/CorrelationRatio_HBHE', 'description' : 'Hcal/HBHE Data/Emulator Correlation Ratio'},{'path' : 'HcalTPTask/Et/CorrRatiovsLS_TPSubDet/CorrelationRatio_HF', 'description' : 'Hcal/HF Data/Emulator Correlation Ratio'}])

hcallayout(dqmitems, '13 HCAL TP Et Correlation 2D
', [{'path' : 'HcalTPTask/Et/Correlation_TPSubDet/Et_DatavsEmul_HBHE', 'description' : 'Hcal/HBHE Et Correlation'},{'path' : 'HcalTPTask/Et/Correlation_TPSubDet/Et_DatavsEmul_HF', 'description' : 'Hcal/HF Et Correlation'}])

hcallayout(dqmitems, '13 HCAL TP Number of Mismatches vs LS
', [{'path' : 'HcalTPTask/Et/MismatchedvsLS_TPSubDet/EtMismatched_HBHE', 'description' : 'Hcal/HBHE Number of Et Mismatches per Event vs LS'},{'path' : 'HcalTPTask/Et/MismatchedvsLS_TPSubDet/EtMismatched_HF', 'description' : 'Hcal/HF Number of Et Mismatches per Event vs LS'}])

