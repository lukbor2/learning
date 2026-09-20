# First example about attribute assignment 

class Accesscontrol:
	def __setattr__(self, attr, value):
		if attr == 'age':
			self.__dict__[attr] = value + 10 # do not use . notation to avoid infinite loop
		else:
			raise AttributeError(attr + ' not allowed.')

if __name__ == '__main__':
	X = Accesscontrol()
	X.age = 40
	print(X.age) # this will print 50
	print(X.name) # this will trigger an error
