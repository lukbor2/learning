#!python

class ListInherited:
    """
    Use dir() to collect both instance attr and names inherited from 
    its classes;
    In this version the print layout is modified.
    """

    def __attrnames(self, indent = ' ' * 4):
        result = 'Under%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr) 
            else:
                display = str(getattr(self, attr))[:82-len(indent) + len(attr)]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)