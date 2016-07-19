#!/usr/bin/python

import sys, os
import ROOT as R
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import DQMIO.Parser as P
import DQMIO.Filter as F
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import glob
import Utils.Shell as Shell
import Utils.RE as RE

def test():
    pathnames = glob.glob("/Users/vk/software/HCALDQM/data/ml/reproduce/*Hcal_*.root")
    l = []; runs = []
    for x in pathnames:
        path, filename = Shell.split(x)
        runNumber = RE.match_filename(filename)["run"]
        if x == "/Users/vk/software/HCALDQM/data/ml/reproduce/DQM_V0001_Hcal_R000273555.root":
            l.insert(0, x)
            runs.insert(0, str(runNumber))
        else:
            l.append(x)
            runs.append(str(runNumber))

    pathnames = l
    print pathnames

#    runs_bad = ["271646", "273730"]
    runs_bad = ["271646"]


    variable = "OccupancyCut"
    tasks={'DigiTask':"DIGI", "RecHitTask":"RECO", "TPTask":"TP"}
    
    frames1 = []; frames2 = [] # each histo is 1 frame
    for pn in pathnames:
        p = P.Parser(pn)
        f = F.Filter(True, module="DigiTask", variable=variable,
            hasher="depth", name="depth1")
        d = p.traverse()
        dd = f.filter(d)
        vals1 = []; vals2 = []
#            for j in range(dd[dd.keys()[0]][0].GetNbinsY()):
        for i in range(dd[dd.keys()[0]][0].GetNbinsX()):
            for j in range(dd[dd.keys()[0]][0].GetNbinsY()):
                vals1.append(dd[dd.keys()[0]][0].GetBinContent(i+1,j+1))
                vals2.append(dd[dd.keys()[0]][0].GetBinError(i+1,j+1))
        frames1.append(vals1); frames2.append(vals2)
    data1 = np.array(frames1)
    data2 = np.array(frames2)

    f = R.TFile("test.root", "recreate")
    hS = []
    runsToLabel = []
    for i in range(len(runs)):
        h = R.TH1D("S_"+runs[i], "S_"+runs[i], 2000, -100, 100)
        hS.append(h)

    s_m_good = []; s_rms_good = []
    s_m_bad = []; s_rms_bad = []
    integrals = data1.sum(axis=1)
    for i in range(data1.shape[0]):
        print "processing Run: " + runs[i]
        summ = 0; summ2=0;
        k = integrals[0]/integrals[i]
        n_eff = 0
        for j in range(data1.shape[1]):
            if data1[0,j]>0 and data1[i,j]>0:
                s = (data1[0,j] - k*data1[i,j])/sqrt(
                    data2[0,j]*data2[0,j] + k*k*data2[i,j]*data2[i,j])
                summ += s
                summ2 += s*s
                n_eff+=1
                hS[i].Fill(s)
        mean = summ/n_eff
        if runs[i] in runs_bad:
            s_m_bad.append(mean)
            s_rms_bad.append(sqrt(summ2/n_eff - mean*mean))
        else:
            s_m_good.append(mean)
            s_rms_good.append(sqrt(summ2/n_eff - mean*mean))
            runsToLabel.append(runs[i])

    #   draw
    plt.plot(s_m_good, s_rms_good, "go")
    plt.plot(s_m_bad, s_rms_bad, "ro")
    plt.title("HCAL DQM Clusterization for Variable: "+variable)
    plt.xlabel("<S>")
    plt.ylabel("sigma_S")

    for x, label, y in zip(s_m_good, runsToLabel, s_rms_good):
       plt.annotate(label, xy=(x,y), xytext=(-10,10), 
            textcoords='offset points',
            arrowprops=dict(arrowstyle="->"))

    plt.show()
    s_means_good = np.array(s_m_good)
    s_rmss_good = np.array(s_rms_good)
    s_means_bad = np.array(s_m_bad)
    s_rmss_bad = np.array(s_rms_bad)
    print "GOOD ONES: "
    print s_means_good, s_rmss_good
    print ""; print "";
    print "BAD ONES: "
    print s_means_bad, s_rmss_bad
    print ""; print "";

    f.Write()
    f.Close()

if __name__=="__main__":
    test()
