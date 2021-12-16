import os
import sys
import configparser
from zipfile import ZipFile

results = open("Log4J_Search_Results.txt", "wt")

#Searches the directory given as the parameter.
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
	
		#Puts the filename into lowercase for easier identification.
		name.lower();
		
		#If the files starts with 'log4j' and ends with 'jar' proceed with version identification.
		if name.startswith("log4j") and name.endswith("jar"):
			filepath = root + "\\" + name
			
			#extracts the required manifest file from the JAR file.
			zipper = ZipFile(filepath, "r")
			zipper.extract("META-INF/MANIFEST.MF")
			
			#Reads the contents of a file to a list and insert a section header at the beginning.
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
			
			#Prints to standard out
			print("File found at: " + filepath)
			print("Log4J Version is: " + manifestParser.get("Deafult","Implementation-Version") + "\n\n")
			
			#Writes results to file.
			results.write("File found at: " + filepath + "\n")
			results.write("Log4J Version is: " + manifestParser.get("Deafult","Implementation-Version") + "\n\n")
			
			#Cleans up after itself.
			os.remove("META-INF/MANIFEST.MF")
			os.removedirs("META-INF")

#Closes the results file cleanly.			
results.close()

exit(0)