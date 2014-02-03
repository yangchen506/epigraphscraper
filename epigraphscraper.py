
#see readme file before using! 

#libraries & Global variables -----------------------------------------------------
from bs4 import BeautifulSoup            #BeautifulSoup parses XML tags.  http://www.crummy.com/software/BeautifulSoup/
from os import walk, getcwd, listdir     #used to grab all files in directory of script
from os.path import isfile, join         #also used in grabbing all files in directory
import os                                
import csv                               #used to interact with csv files (not yet working)
totalEpigraphCount = 0                   #counts total number of epigraphs in all files in directory
epigraphlessFileCount = 0                #counts total number of files in directory that do not have epigraphs

#get list of files in current directory & put it in an array ---------------------
allFilesInDirectory = [ i for i in listdir(getcwd()) if isfile(join(getcwd(),i)) ]

#scrape epigraphs from all XML files----------------------------------------------
for x in xrange(0, len(allFilesInDirectory)):                   #loop through all files in directory
    root, ext = os.path.splitext(allFilesInDirectory[x])        #select file extension for particular file "x" in the list "allFilesInDirectory"
    if (ext == '.xml'):                                         #if file ends in ".xml", read file 
       
    # open file "x" to be read ---------------------------------------------------
       readfile = open(str(allFilesInDirectory[x]))	        #specify file "x" to be read & open file
       soup = BeautifulSoup(readfile)                           #make "soup" object of file to search 
       
    # strip author & epigraphs from individual file-------------------------------
       authorlist = [author.text for author in soup('author')]          #collect entries tagged "author" and place it in the list "authorlist"
       epigraphlist = [epigraph.text for epigraph in soup('epigraph')]  #collect entries tagged "epigraph" and place it in the list "epigraphlist" 

    # close file------------------------------------------------------------------
       readfile.close()                                                 #close file "x"
    
    # calculate statistics & output all information to terminal ------------------
       if (len(soup.findAll('epigraph')) == 0):                         #check if file has epigraphs and record this                
          #print allFilesInDirectory[x] + ": No epigraphs found."       #Error Test
          epigraphlessFileCount += 1
       else:                                                            #file has epigraphs, print hypertext author, hypertext title, and epigraph to terminal
          for i in xrange(0, len(soup.findAll('epigraph'))):
             if (len(soup.findAll('author')) == 0):
                 print "Unknown Author" + "    " + allFilesInDirectory[x] + "    " + str(i+1) + "   " + epigraphlist[i]
                 totalEpigraphCount += 1
             else:    
                 print authorlist[0] + "    " + allFilesInDirectory[x] + "    " + str(i+1) + "   " + epigraphlist[i]
                 totalEpigraphCount += 1

#Print total number of epigraphs collected to the terminal-------------------------
print "TOTAl NUMBER OF EPIGRAPHS: " + str(totalEpigraphCount)
print "TOTAL NUMBER OF FILES: " + str(len(allFilesInDirectory))
print "FILES WITHOUT EPIGRAPHS: " + str(epigraphlessFileCount)

#CODE SNIPPETS THAT MAY BE USEFUL FOR FUTURE CHANGES-------------------------------
#Can directly access individual epigraph as follows:
#soup('author')[0].text
#soup('author')[1].text
#soup('epigraph')[0].text
#soup('epigraph')[1].text
#THIS SHOULD WORK: out.writerow(authorlist[2] + "    " + allFilesInDirectory[x] + "    "
# + str(i) + "   " + epigraph[i])
#out = csv.writer(open("epigraph.csv","wb"), delimiter='\t',quoting=csv.QUOTE_MINIMAL) 
