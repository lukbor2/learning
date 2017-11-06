# ElementTree is the key library to import.
# More info here:
# https://docs.python.org/3/library/xml.etree.elementtree.html
# http://effbot.org/zone/element-index.htm
# There is a library which can be used to read / write csv files. In case I want to convert a xml into csv for example.
# https://docs.python.org/3/library/csv.html


import xml.etree.ElementTree as ET
import csv

tree = ET.parse('country_data.xml') # country_data.xml is a test xml file I am using as an example.
root = tree.getroot() 

print(root.tag) # root is an Element and a tag attribute.

# root has children, each children is an element with tags and attributes.
for child in root:
    print(child.tag, child.attrib)

# children are nested and can be accessed with index. This should return '2008' .
print(root[0][1].text) 

# Element allows to iterate on any level of the tree.
for neighbor in root.iter('neighbor'): 
    print(neighbor.tag, neighbor.attrib)

for gdppc in root.iter('gdppc'):
    print(gdppc.tag , gdppc.text)

# findall() returns all childern of current element with a specific tag.
# find() finds the first child with a particular tag.
# get() accesses the attributes of the element.
 
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

# Trying to use the csv library now.

# Reading and printing each line of a .csv file.
with open ('units_of_measure.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Writing into a simple .csv file
with open ('test_csv_write.csv', 'w') as f:
    writer = csv.writer(f)
    head = ['Name', 'Surname', 'Place of Birth'] # This is the header.
    writer.writerow(head) # Writing just one row.

    record_1 = ['Luca', 'Borghi', 'Modena']
    record_2 = ['Lorenzo', 'Manuguerra', 'Collecchio']
    data = [record_1, record_2]
    writer.writerows(data)

# Now, trying to write a csv file from the test xml I am using.

f = open('country_test.csv', 'w')
writer = csv.writer(f)

head = ['Country_Name', 'Country_Rank', 'Year', 'Country_gdppc'] # This is the header.
writer.writerow(head)

for country in root.findall('country'):
    data = [country.get('name'), country.find('rank').text, country.find('year').text, country.find('gdppc').text]
    writer.writerow(data)
