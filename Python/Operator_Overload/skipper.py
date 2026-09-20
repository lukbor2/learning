# runs in Python 3 only
# in this example the iterable object allows multiple active iteration loops
# because a new instance of the object is created for each iteration

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator:
    def __init__(self, wrapped):
       self.wrapped = wrapped
       self.offset = 0
    def __next__(self):
       if self.offset >= len(self.wrapped):
           raise StopIteration
       else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

if __name__ == "__main__":
    alpha = "abcdef"
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I)) 

    for x in skipper:
        for y in skipper:
            print(x + y, end = ' ')
