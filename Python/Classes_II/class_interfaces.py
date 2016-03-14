class Super:
    def method(self):
        print('in Super.method') # default behavior
    def delegate(self):
        self.action() # this method expects to be defined in a sub-class
    
    def action(self): # this is a way to raise an exception in case the action method is not implemented by a sub-class
        assert False, 'action must be defined'
        
"""
    this is another way of checking whether the action method has been implemented by a sub-class
    
    def action(self):
        raise NotImplementedError('action must be defined')
        
"""
        
class Inheritor(Super): # just inherits methods
    pass

class Replacer(Super): # replace method of the super-class completely
    def method(self):
       print('in Replacer.method') 
       
class Extender(Super): # extend method behavior
    def method(self):
      print('starting Extender.method')
      Super.method(self)  
      print('ending Extender.method')
      
class Provider(Super): # fill in a required method
    def action(self):
        print('in Provider.action')
        
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender): # note how I can create a tuple with the classes and iterate it
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    X = Super()
    X.delegate()