# Example showing how to implement a string representation
# Here I implement both __str__ and __repr__ methods

class adder:
	def __init__(self, value = 0):
		self.data = value
	def __add__(self, other):
		self.data += other 

class addboth(adder):
	def __str__(self):
		return '[Value: %s]' % self.data
	def __repr__(self):
		return 'addboth(%s)' % self.data

if __name__ == '__main__':
	x = addboth(4)
	x + 1
	print(x) # uses __str__
	print(repr(x)) # uses __repr__
