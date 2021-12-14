import os
import sys

from zipfile import ZipFile
import configparser

jarFile = sys.argv[1]
if os.path.isfile(jarFile):
	zipper = ZipFile(jarFile, "r")
	zipper.extract("META-INF/MANIFEST.MF")

	file = open("META-INF/MANIFEST.MF", "r")
	temp = file.readlines()
	temp.insert(0, "[Deafult]\n")
	file.close()

	file = open("META-INF/MANIFEST.MF", "wt")
	for line in temp:
		file.write(line)
	file.close()

	manifestParser = configparser.ConfigParser(delimiters=':',strict=False)
	manifestParser.read_file(open("META-INF/MANIFEST.MF", "rt"))
	print("Log4J Version is: " + manifestParser.get("Deafult","Implementation-Version"))
else:
	print("File Doesn't Exist!")