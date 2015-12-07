#!/usr/bin/python

#
#	HCAL Generic Id class
#

class Id:
	"""
	"""
	def __init__(self, id):
		"""
		"""
		self.id = id
		self.repr = "<Id %d>" % self.id

	def __repr__(self):
		return self.repr

	def __eq__(self, other):
		return hash(self.id)==hash(other.id)

	def __hash__(self):
		return self.id


#	testing
if __name__=="__main__":
	id1 = Id(0)
	id2 = Id(1)
	id3 = Id(0)
	print(id1)
	print(id2)
	print(id1==id2)
	print(id1==id3)

