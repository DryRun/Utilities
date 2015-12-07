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

hcallayout(dqmitems, '01 HCAL  Summary', [{'path' : 'Hcal/RawTask/Summary/Summary', 'description' : 'HCAL RAW Format Summary per FED'},{'path' : 'Hcal/RecHitTask/Summary/Summary', 'description' : 'HCAL REC HIT Format Summary per SubDetetor'}],[{'path' : 'Hcal/DigiTask/Summary/Summary', 'description' : 'HCAL DIGI Format Summary per SubDetetor'},{'path' : 'Hcal/TPTask/Summary/Summary', 'description' : 'HCAL Trigger Primitive Format Summary per SubDetetor'}])

hcallayout(dqmitems, '02 HCAL DIGI Occupancy vs LS', [{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HB', 'description' : 'HB Occupancy vs LS'},{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HE', 'description' : 'HE Occupancy vs LS'}],[{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HF', 'description' : 'HF Occupancy vs LS'},{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HO', 'description' : 'HO Occupancy vs LS'}])

hcallayout(dqmitems, '03 HCAL DIGI Occupancy 2D', [{'path' : 'Hcal/DigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth1', 'description' : 'Depth 1 Occupancy.'},{'path' : 'Hcal/DigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth2', 'description' : 'Depth 2 Occupancy.'}],[{'path' : 'Hcal/DigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth3', 'description' : 'Depth 3 Occupancy.'},{'path' : 'Hcal/DigiTask/Occupancy/depth_SumQHBHE20HO20HF20/Occupancy_Depth4', 'description' : 'Depth 4 Occupancy.'}])

hcallayout(dqmitems, '04 HCAL DIGI Missing Channels per 1LS', [{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth1', 'description' : 'Depth 1 Missing channels per 1LS. Updated each 10LS'},{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth2', 'description' : 'Depth 2 Missing channels per 1LS. Updated each 10LS'}],[{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth3', 'description' : 'Depth 3 Missing channels per 1LS. Updated each 10LS'},{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth4', 'description' : 'Depth 4 Missing channels per 1LS. Updated each 10LS'}])

hcallayout(dqmitems, '05 HCAL DIGI Missing Channels per 1LS vs LS', [{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HB', 'description' : 'Number of HB missing channels per 1LS.'},{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HE', 'description' : 'Number of HE missing channels per 1LS.'}],[{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HF', 'description' : 'Number of HF missing channels per 1LS.'},{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HO', 'description' : 'Number of HO missing channels per 1LS.'}])

hcallayout(dqmitems, '06 HCAL RECHIT Timing 2D', [{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth1', 'description' : 'Depth 1 Timing.'},{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth2', 'description' : 'Depth 2 Timing.'}],[{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth3', 'description' : 'Depth 3 Timing.'},{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth4', 'description' : 'Depth 4 Timing.'}])

hcallayout(dqmitems, '07 HCAL RECHIT HBHEabc Timing', [{'path' : 'Hcal/RecHitTask/Timing/HBHEPartition_EHBHE5HO5HF5/Timing_HBHEa', 'description' : 'HBHEa Timing'},{'path' : 'Hcal/RecHitTask/Timing/HBHEPartition_EHBHE5HO5HF5/Timing_HBHEb', 'description' : 'HBHEb Timing'},{'path' : 'Hcal/RecHitTask/Timing/HBHEPartition_EHBHE5HO5HF5/Timing_HBHEc', 'description' : 'HBHEc Timing'}])

hcallayout(dqmitems, '08 HCAL RECHIT Energy 2D', [{'path' : 'Hcal/RecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth1', 'description' : 'Depth 1 Energy'},{'path' : 'Hcal/RecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth2', 'description' : 'Depth 2 Energy'}],[{'path' : 'Hcal/RecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth3', 'description' : 'Depth 3 Energy'},{'path' : 'Hcal/RecHitTask/Energy/depth_EHBHE5HO5HF5/Energy_Depth4', 'description' : 'Depth 4 Energy'}])

hcallayout(dqmitems, '09 HCAL RECHIT Energy per SubDetector', [{'path' : 'Hcal/RecHitTask/Energy/SubDet/Energy_HB', 'description' : 'Energy HB'},{'path' : 'Hcal/RecHitTask/Energy/SubDet/Energy_HE', 'description' : 'Energy HE'}],[{'path' : 'Hcal/RecHitTask/Energy/SubDet/Energy_HF', 'description' : 'Energy HF'},{'path' : 'Hcal/RecHitTask/Energy/SubDet/Energy_HO', 'description' : 'Energy HO'}])

hcallayout(dqmitems, '10 HCAL TP Occupancy vs LS', [{'path' : 'Hcal/TPTask/Occupancy/DatavsLS_TPSubDet/Occupancy_Data_HBHE', 'description' : 'HBHE Data TPs Occupancy vs LS'},{'path' : 'Hcal/TPTask/Occupancy/DatavsLS_TPSubDet/Occupancy_Data_HF', 'description' : 'HF Data TPs Occupancy vs LS'}],[{'path' : 'Hcal/TPTask/Occupancy/EmulvsLS_TPSubDet/Occupancy_Emul_HBHE', 'description' : 'HBHE Emulator TPs Occupancy vs LS'},{'path' : 'Hcal/TPTask/Occupancy/EmulvsLS_TPSubDet/Occupancy_Emul_HF', 'description' : 'HF Emulator TPs Occupancy vs LS'}])

hcallayout(dqmitems, '11 HCAL TP Occupancy 2D', [{'path' : 'Hcal/TPTask/Occupancy/Occupancy_Data', 'description' : 'Data Occupancy'},{'path' : 'Hcal/TPTask/Occupancy/Occupancy_Emul', 'description' : 'Emulator Occupancy'}])

hcallayout(dqmitems, '12 HCAL TP Et Correlation vs LS', [{'path' : 'Hcal/TPTask/Et/CorrRatiovsLS_TPSubDet/CorrelationRatio_HBHE', 'description' : 'HBHE Data/Emulator Correlation Ratio'}],[{'path' : 'Hcal/TPTask/Et/CorrRatiovsLS_TPSubDet/CorrelationRatio_HF', 'description' : 'HF Data/Emulator Correlation Ratio'}])

hcallayout(dqmitems, '13 HCAL TP Et Correlation 2D', [{'path' : 'Hcal/TPTask/Et/Correlation_TPSubDet/Et_DatavsEmul_HBHE', 'description' : 'HBHE Et Correlation'},{'path' : 'Hcal/TPTask/Et/Correlation_TPSubDet/Et_DatavsEmul_HF', 'description' : 'HF Et Correlation'}])

hcallayout(dqmitems, '13 HCAL TP Number of Mismatches vs LS', [{'path' : 'Hcal/TPTask/Et/MismatchedvsLS_TPSubDet/Mismatched_HBHE', 'description' : 'HBHE Number of Et Mismatches per Event vs LS'}],[{'path' : 'Hcal/TPTask/Et/MismatchedvsLS_TPSubDet/Mismatched_HF', 'description' : 'HF Number of Et Mismatches per Event vs LS'}])

