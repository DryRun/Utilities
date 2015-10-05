import FWCore.ParameterSet.Config as cms

process = cms.Process("DUMP")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")

import sys
print sys.argv
runNumber = int(sys.argv[2])
record = sys.argv[3]
tag	= sys.argv[4]
gateway = sys.argv[5]

process.maxEvents = cms.untracked.PSet(
		    input = cms.untracked.int32(1)
			)

process.source = cms.Source("EmptySource",
		    numberEventsInRun = cms.untracked.uint32(1),
			    firstRun = cms.untracked.uint32(runNumber)
				)

process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
		    dump = cms.untracked.vstring(''),
			    file = cms.untracked.string('')
				)

process.es_pool = cms.ESSource("PoolDBESSource",
		    process.CondDBSetup,
			    timetype = cms.string('runnumber'),
				    toGet = cms.VPSet(
						cms.PSet(
							record = cms.string("Hcal%sRcd" % record),
							tag = cms.string(tag)
							)
					),
					connect = cms.string(gateway),
					authenticationMethod = cms.untracked.uint32(0),
)

process.dumpcond = cms.EDAnalyzer("HcalDumpConditions",
		       dump = cms.untracked.vstring(record),
			   outFilePrefix = cms.untracked.string('Dump_%s_' % tag)
			   )
process.p = cms.Path(process.dumpcond)

