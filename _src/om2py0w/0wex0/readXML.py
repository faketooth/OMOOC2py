# -*- coding: utf-8 -*-
# learn how to parse a xml file with ElementTree

import xml.etree.cElementTree as ET
import sys

tree = ET.ElementTree(file='test.xml')
root = tree.getroot()
print root.tag, root.attrib
# 遍历root的子节点文件
for element in root:
	print 'tag is %s, attrib is %s' % (element.tag, element.attrib)
	
# 深度优先遍历
print '-' * 10
for e in tree.iter():
	print 'tag is %s, attrib is %s' % (e.tag, e.attrib)
	
# XPath

# dump xml file
tree.write(sys.stdout)
print 
# create new xml 
print '=' * 10
new_root = ET.Element('root')
new_root.extend((root[0], root[2]))
tree_new = ET.ElementTree(new_root)
tree_new.write(sys.stdout)
tree_new = ET.ElementTree(root[-1])
tree_new.write(sys.stdout)