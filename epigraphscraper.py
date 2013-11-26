
#see readme file before using! 

#libraries & Global variables ----------------------------------------------------
from bs4 import BeautifulSoup
from os import walk, getcwd, listdir
from os.path import isfile, join
import os
import csv
totalEpigraphCount = 0
epigraphlessFileCount = 0
#out = csv.writer(open("epigraph.csv","wb"), delimiter='\t',quoting=csv.QUOTE_MINIMAL)

#get only files from directory & loop through each file --------------------------
allFilesInDirectory = [ i for i in listdir(getcwd()) if isfile(join(getcwd(),i)) ]

for x in xrange(0, len(allFilesInDirectory)):
    root, ext = os.path.splitext(allFilesInDirectory[x])
    if (ext == '.xml'):
       
    # open file to be read -------------------------------------------------------
       readfile = open(str(allFilesInDirectory[x]))	#specific file to be examined
       soup = BeautifulSoup(readfile) #make file "soup" object for easy searching
       
    # strip author & epigraphs from individual file-------------------------------
       authorlist = [author.text for author in soup('author')]  #collect author entries 
       epigraphlist = [epigraph.text for epigraph in soup('epigraph')]  #collect epigraphs 

    # close file------------------------------------------------------------------
       readfile.close()
    
    # print out contents to terminal ---------------------------------------------
       if (len(soup.findAll('epigraph')) == 0):
          #print allFilesInDirectory[x] + ": No epigraphs found." #Error Test
          epigraphlessFileCount += 1
       else:
          for i in xrange(0, len(soup.findAll('epigraph'))):
             if (len(soup.findAll('author')) == 0):
                 print "Unknown Author" + "    " + allFilesInDirectory[x] + "    " + str(i+1) + "   " + epigraphlist[i]
                 totalEpigraphCount += 1
             else:    
                 print authorlist[0] + "    " + allFilesInDirectory[x] + "    " + str(i+1) + "   " + epigraphlist[i]
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
