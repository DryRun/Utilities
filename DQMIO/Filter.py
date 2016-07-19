#!/usr/bin/python

#
#	ROOT DQM TH1-like Filter
#

import sys, os
import ROOT as R
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import Utils.RE as RE
import Settings.AnalysisModules as settings

#	define the Filter class
class Filter:
    """
    Filter Class : given a dictionary of objects, filters out based on tokens
    if isPreserver:
        preserves based on tokens
    else:
        skips based on tokens
    """

    def __init__(self,  isPreserver, variable=0, hasher=0, module=0,
        name=0): 
        self.isPreserver = isPreserver
        self.tokens = {"variable":variable, "hasher":hasher, "module":module,
            "name":name}

    def filter(self, objs):
	r = {}
	for path in objs.keys():
            tokens = RE.match_path(path)
            #   this is basically filtering out non-HCAL format
            if tokens["module"] not in settings.modules:
                continue
            #   ^^^

            for o in objs[path]:
                tokens["name"] = o.GetName()

                #   simple logic
                nskipped=0; nms=0
                for key in self.tokens.keys():
                    if self.tokens[key]==0:
                        nskipped+=1
                    elif self.tokens[key]==tokens[key]:
                        nms+=1
                if nms+nskipped==len(self.tokens.keys()):
                    if self.isPreserver:
                        if path in r.keys():
                            r[path].append(o)
                        else:
                            r[path] = [o]
                else:
                    if not self.isPreserver:
                        if path in r.keys():
                            r[path].append(o)
                        else:
                            r[path] = [o]
        return r

if __name__=="__main__":
    import Parser
    parser = Parser.Parser("/Users/vk/software/HCALDQM/data/DQM_V0001_Hcal_R000273554.root")
    f = Filter(True, module="RawTask")
    d = parser.traverse()
    d = f.filter(d)
    print d
