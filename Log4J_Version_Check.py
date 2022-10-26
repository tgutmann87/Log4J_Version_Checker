import os
import re
import sys
import shutil
import configparser
from zipfile import ZipFile

def checkLog4J(filepath, results = ""):
	for root, dirs, files in os.walk(filepath):
		for name in files:
			name.lower()
			if name.startswith("log4j") and name.endswith("jar"):
				print(results)
				
				#Extracting the manifest file from the JAR archive
				zipper = ZipFile(root + "\\" + name, "r")
				zipper.extract("META-INF/MANIFEST.MF")
				
				#Places a header for the ConfigParser
				file = open("META-INF/MANIFEST.MF", "r")
				temp = file.readlines()
				temp.insert(0, "[Deafult]\n")
				file.close()
				
				#Write the changes to the file.
				file = open("META-INF/MANIFEST.MF", "wt")
				for line in temp:
					file.write(line)
				file.close()
				
				#Uses a configuration parser to read the modified file and parse the version.
				#WARNING: This part is unstable because the parser is not following enforced standards due to the 'strict=False' parameter.
				manifestParser = configparser.ConfigParser(delimiters=':',strict=False)
				manifestParser.read_file(open("META-INF/MANIFEST.MF", "rt"))
				
				#Adds finding to total results
				results += "File found at: " + root + "\\" + name + "\n"
				results += "Log4J Version is: " + manifestParser.get("Deafult","Implementation-Version") + "\n\n"
				
				shutil.rmtree("META-INF")
			
			elif re.search("jar$", name):
				zipper = ZipFile(root + "\\" + name, "r")
				zipDir = zipper.infolist()
				
				for i in zipDir:
					if i.is_dir() and not i.filename == "META-INF":
						zipper.extract(i.filename, "Log4JChecker_Temp")
						results = checkLog4J("Log4JChecker_Temp\\" + i.filename, results)
						shutil.rmtree("Log4JChecker_Temp\\" + i.filename)
						
						
	return results
	
	
#####Actual Program Start#####	
if not os.path.exists("Log4JChecker_Temp"):
	os.mkdir("Log4JChecker_Temp")
	
file = open("Log4J_Search_Results.txt", "wt")
file.write(checkLog4J(sys.argv[1]))

if os.path.exists("Log4JChecker_Temp"):
	shutil.rmtree("Log4JChecker_Temp")

file.close()