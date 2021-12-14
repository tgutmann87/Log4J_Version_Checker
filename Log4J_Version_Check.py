import os
import sys

from zipfile import ZipFile
import configparser

jarFile = sys.argv[1]
zipper = ZipFile(jarFile, "r")
#print(zipper.getinfo("META-INF/MANIFEST.MF"))
zipper.extract("META-INF/MANIFEST.MF")

file = open("META-INF/MANIFEST.MF", "r")
temp = file.readlines()
temp.insert(0, "[Deafult]\n")
file.close()

file = open("tempManifest.txt", "wt")
for line in temp:
	file.write(line)
file.close()

manifestParser = configparser.ConfigParser(delimiters=':',strict=False)
manifestParser.read_file(open("tempManifest.txt", "rt"))
#print(manifestParser.sections())
print(manifestParser.get("Deafult","Implementation-Version"))
