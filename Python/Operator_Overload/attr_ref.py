# First example about attribute reference

class Empty:
	def __getattr__(self, attrname):
		if attrname == 'age':
			return 40
		else:
			raise AttributeError(attrname)

if __name__ == '__main__':
	X = Empty()
	print(X.age)
	print(X.name) # this will generate an error
