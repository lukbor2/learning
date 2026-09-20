from gi.overrides.keysyms import union

class Adder:
    def add(self, x, y):
        print('Not implemented here...')
        
    def __init__(self, start=[]):
        self.data = start
        
    def __add__(self, other): # This is a "special" method. It will be used every time this class or its sub-classes are used with the + operator
        return self.add(self.data, other)
        
class ListAdder(Adder):
    def add(self, x, y):
        if type(x) == list and type(y) == list:
            return(x+y)
        else:
            print('Arguments are not lists')
            
class DictAdder(Adder):
    def add(self, x, y):
        if type(x) == dict and type(y) == dict:
            union = x.copy()
            union.update(y)
            return union
        else:
            print('Arguments are not dictionaries')