#!/usr/bin/python

import sys, os, getopt
form = "./dowload.py -h -r <csv runlist> -c <cert key> -a <hcal dqm app name>"

try:
	opts, args = getopt.getopt(sys.argv[1:], "hr:c:a:", ["help=", "runlist=", "cert=", "app="])
except getopt.GetoptError:
    print "GetoptError Exception.";print form;sys.exit(2)

runlist = []; cert_key = ""
for opt, arg in opts:
	if opt=="-r": 
		runlist = arg.split(",")
	elif opt=="-h":
		print form
		sys.exit(2)
	elif opt=="-c":
		cert_key = arg
	elif opt=="-a":
		appname = arg

if runlist==[] or cert_key=="" or cert_key=="None":
    print "Either run list is empty or no certificate is provided. Exiting..."
    sys.exit(2)

print "### Starting Downloading"
for x in runlist:
	format1 = "000%dxxxx" % (int(x)/10000)
	format2 = "000%dxx" % (int(x)/100)
	filename = "DQM_V0001_%s_R000%d.root" % (appname, int(x))
	f = {"FORMAT1" : format1, "FORMAT2" : format2, "FILENAME" : filename,
		"CERT_KEY": cert_key}
	cmd = "curl -O -L --capath %(CERT_KEY)s --key %(CERT_KEY)s --cert %(CERT_KEY)s https://cmsweb.cern.ch/dqm/online/data/browse/Original/%(FORMAT1)s/%(FORMAT2)s/%(FILENAME)s" % f
	os.system(cmd)

