import xml.etree.ElementTree as ET
import re

file_xml = '/home/rahi/pycode/how_to_import_data/JSON_XML/users-100.xml'
tree = ET.parse(source=file_xml)
print(tree)

users_root = tree.getroot()
print(users_root.tag)
print(len(users_root.getchildren())) 


# find element
print(users_root[0].tag)
print(users_root[0].attrib)
