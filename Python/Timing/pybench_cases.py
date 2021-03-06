import pybench, sys

pythons = [
        (1, '/usr/bin/python3'),
        (0, '/usr/bin/python'),
        (0, '/usr/bin/python')
    ]

stmts = [
    (0,0, "[x ** 2 for x in range(1000)]"),
    (0,0, "res=[]\nfor x in range(1000): res.append(x**2)"),
    (0,0, "$listif3(map(lambda x: x ** 2, range(1000)))"),
    (0,0, "list(x ** 2 for x in range(1000))"),
    ]
    
tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)