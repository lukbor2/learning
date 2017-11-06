# ElementTree is the key library to import.
# More info here:
# https://docs.python.org/3/library/xml.etree.elementtree.html
# http://effbot.org/zone/element-index.htm

import xml.etree.ElementTree as ET

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
