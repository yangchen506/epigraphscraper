
#--------------------------------------------------------------------------------
#READ THIS FIRST BEFORE USING!!
#This script pulls all author entries & epigraphs from all the XML
#files in a directory in which this program is executed.
#(1) Include  ONLY XML files in the directory you want to 
#strip for data *disaster unmitigated* may occur.
#(2) DO NOT include any subfolders. 
#(3) The current working directory of your terminal needs to be the 
#same directory that your script it is! 
#(4) This file best viewed with truncated (i.e., not word wrapped) lines
#(5) This script was written and tested on OS X. It'll probably work in unix.
#I haven't tested it. No promises. 
#---------------------------------------------------------------------------------

#Wish list------------------------------------------------------------------------
#(1) need to grab all the other attributes like title, year, etc.
#(2) output to a csv file

#libraries & Global variables ----------------------------------------------------
from bs4 import BeautifulSoup
from os import walk, getcwd, listdir
from os.path import isfile, join
import os
import csv

totalEpigraphCount = 0
epigraphlessFileCount = 0
out = csv.writer(open("epigraph.csv","wb"), delimiter='\t',quoting=csv.QUOTE_MINIMAL)

#get only files from directory & loop through each file --------------------------
allFilesInDirectory = [ i for i in listdir(getcwd()) if isfile(join(getcwd(),i)) ]

for x in range(0, len(allFilesInDirectory)):
    root, ext = os.path.splitext(allFilesInDirectory[x])
    if (ext == '.xml'):
       
    # open file to be read -------------------------------------------------------
       readfile = open(str(allFilesInDirectory[x]))	#specific file to be examined
       soup = BeautifulSoup(readfile) #make file "soup" object for easy searching
       
    # strip author & epigraphs from individual file-------------------------------
       numberOfAuthorEntries = len(soup.findAll('author'))	# number of hypertext author entries
       authorlist = [soup('author')[e].text for e in range(numberOfAuthorEntries)]  #collect "author"s
       numberOfEpigraphs = len(soup.findAll('epigraph'))    # number of epigraphs in file
       epigraph = [soup('epigraph')[e].text for e in range(numberOfEpigraphs)]	#collect epigraphs
       readfile.close()
    
    # print out contents to terminal --------------------------------------------
       if (len(soup.findAll('epigraph')) == 0):
          #print allFilesInDirectory[x] + ": No epigraphs found."
          epigraphlessFileCount += 1
       else:
          for i in range(0,len(soup.findAll('epigraph'))):
             print authorlist[1] + "    " + allFilesInDirectory[x] + "    " + str(i) + "   " + epigraph[i]
             totalEpigraphCount += 1

print "TOTAl NUMBER OF EPIGRAPHS: " + str(totalEpigraphCount)
print "TOTAL NUMBER OF FILES: " + str(len(allFilesInDirectory))
print "FILES WITHOUT EPIGRAPHS: " + str(epigraphlessFileCount)

#Notes for future changes--------------------------
#Can directly access individual epigraph as follows:
#soup('author')[0].text
#soup('author')[1].text
#soup('epigraph')[0].text
#soup('epigraph')[1].text
#THIS SHOULD WORK: out.writerow(authorlist[2] + "    " + allFilesInDirectory[x] + "    "
# + str(i) + "   " + epigraph[i])
