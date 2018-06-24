
class MyList():
    def __init__(self, l=[]):
       self.data = list(l) #make sure it is a list

    def __add__(self, y):
        return MyList(self.data +y) #I want to return a MyLyst object, not a list

    def __repr__(self): # This is to be able to print an instance of MyList
        return repr(self.data)
    
    def __mul__(self, time):
        return MyList(self.data * time) #I want to return a MyLyst object, not a list
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)
    
    def __getslice__(self, low, high):
        return MyList(self.data[low:high])
    
    def append(self,l):
        self.data.append(l)
        
    def __getattr__(self, name): #To understand this code see the explanation below about getattr.
        return getattr(self.data, name)

'''
    Consider how getattr works
  
    result = obj.method(args)
    func = getattr(obj, "method")
    result = func(args)

     or, in one line:

    result = getattr(obj, "method")(args)
'''    

if __name__ == '__main__':
    mylist = MyList('spam')
    print(mylist)
    print(mylist.data + [4,5,6])       
    print(mylist.data * 3)       
    print(mylist[2])
    print(len(mylist))
    print(mylist[1:])    
    print(mylist[:1])    
    mylist.append('luca')
    print(mylist)
    mylist.sort()
    print(mylist)