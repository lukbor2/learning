#showing how to use shelve and pickle to permanently store objects

from person_v2 import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb') #name of the file where objects will be stored
for obj in (bob, sue, tom):
    db[obj.name] = obj #will use the object's name as a key
db.close()