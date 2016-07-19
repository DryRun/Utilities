"""
Generic Process Class 
"""

    

class Process:
    def __init__(self, *args, **kwargs):
	self.__name = args[0]
	self.__host = kwargs["host"]
	self.__port = kwargs["port"]
	pass

    def intitialize(self):
	pass

    def execute(self):
        pass

    def finalize(self):
	pass
