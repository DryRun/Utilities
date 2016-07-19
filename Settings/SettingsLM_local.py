"""
module to be imported to grab settings for LMs
"""

lid0["PROCESSINGTYPE"] = "LOCAL"
lid0["HOSTNAME"] = "localhost"
lid0["PORT"] = 30000

lid1["PROCESSINGTYPE"] = "LOCAL"
lid1["HOSTNAME"] = 'localhost'
lid1["PORT"] = 30001
lid1["PROCESSINGMASTERHOSTNAME"] = "localhost"
lid1["PROCESSINGMASTERPORT"] = 20001

settings[lid0, lid1]
