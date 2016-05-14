from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print("<PRE>%s</PRE>" % line.rstrip())


if __name__ == "__main__":
    import sys
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process()
    print()
    
    Uppercase(open('trispam.txt'), HTMLize()).process() #HTMLize is used as writer and implements the method write