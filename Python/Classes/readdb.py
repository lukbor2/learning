#reading from the db

import shelve

db = shelve.open('persondb')
print("Record count: ", len(db))
print("Keys in the db: ", list(db.keys()))

bob = db['Bob Smith']
print(bob)
print(bob.lastName())

for key in db:
    print(key, '=>', db[key])

#notice we do not need to import the Person and Manager class.
#This is because how pickle and shelve work. See page 851 for details