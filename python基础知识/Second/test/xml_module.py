#!/usr/bin/env python3
#coding:utf-8

import xml.etree.ElementTree as ET

root = ET.Element("namelist") #root

name = ET.SubElement(root,"name",arrtib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
n = ET.SubElement(name,"name")
n.text = "zhang chuhan"
sex.text = "male"

et = ET.ElementTree(root)

et.write("build_out.xml",encoding = "utf-8",xml_declaration=True)