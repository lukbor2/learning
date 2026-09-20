"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)

# Test with the interactive prompt
# import docstr
# docstr.__doc__
# docstr.func.__doc__
# docstr.spam.__doc__
# docstr.spam.method.__doc__
# x = docstr.spam()
# x.method()
# help(docstr)