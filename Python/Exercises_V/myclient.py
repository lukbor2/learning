import mymod

testfile = 'testFile.txt'

if mymod.countChars(testfile) == 39:
    print('countChars test is OK')

if mymod.countLines(testfile) == 4:
    print('countLines test is OK')