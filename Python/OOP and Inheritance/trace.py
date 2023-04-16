#Example of a wrapper object and delegation

class Wrapper:
    def __init__(self, object):
        self.wrapped = object
        
    #__getattr__ is called every time an attribute is accessed
    def __getattr__(self, attrname):
        print('Trace: ', attrname)
        return getattr(self.wrapped, attrname)