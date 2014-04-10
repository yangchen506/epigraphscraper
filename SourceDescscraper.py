
#see readme file before using!

#libraries & Global variables ----------------------------------------------------
from bs4 import BeautifulSoup
from os import walk, getcwd, listdir
from os.path import isfile, join
import os
import csv
import re
import sqlite3
import sys

sourceDesclessFileCount = 0
sourceDescerrorFileCount = 0
totalsourceDescCount = 0

#connect to database -------------------------------------------------------------
try:
    db = sqlite3.connect("Epigraph.db")
except sqlite3.Error,e:
    print"Failure to connect the database","\n",e.args[0]

# Name of the data base
# If exists, then open the database; if not, then create it and open it.

# The Cursor object will let you execute the sql commands
cur = db.cursor()

# crete a table with attributes---------------------------------------------------
# If the table exists, delete it and recreate it.
deleteCommand= "DROP TABLE if exists SourceDesc;"
try:
    cur.execute(deleteCommand)
except sqlite3.Error,e:
    print "Failure to delete the talbe." , "\n", e.args[0]

db.commit()


createCommand = "create table SourceDesc(Filename varchar(255) not null, Author varchar(255), Title varchar(255), PubPlace varchar(255), PubDate varchar(255), Publisher varchar(255), primary key(Filename)) ;"
try:
    cur.execute(createCommand)
except sqlite3.Error,e:
    print "Failure to create the talbe." , "\n", e.args[0]

db.commit()

#get only files from directory & loop through each file --------------------------
allFilesInDirectory = [ i for i in listdir(getcwd()) if isfile(join(getcwd(),i)) ]

for x in xrange(0, len(allFilesInDirectory)):
    root, ext = os.path.splitext(allFilesInDirectory[x])
    if (ext == '.xml'):
        
        # open file to be read -------------------------------------------------------
        readfile = open(str(allFilesInDirectory[x]))	#specific file to be examined
        soup = BeautifulSoup(readfile) #make file "soup" object for easy searching
        
        # strip sourceDesc from individual file-------------------------------
        sourceDesc = soup.find_all( 'sourcedesc' )
        # close file------------------------------------------------------------------
        readfile.close()
    
        # print out contents to terminal and database---------------------------------
        if (len(sourceDesc) == 0):
            sourceDesclessFileCount += 1
            print "No SourceDesc Found." "\n"
        elif (len(sourceDesc)>1):
            sourceDescerrorFileCount += 1
            print "More than one SourceDesc Found." "\n"
        else:
            # save title, author, publish place and publish date--------------------------------
            tag = sourceDesc[0].findChild( name='title' )
            if tag:
                title = tag.get_text().strip()
            else:
                title = "Unknown Title"
            
            tag1 = sourceDesc[0].findChild( name='author' )
            tag2 = sourceDesc[0].findChild( name='editor' )
            if tag1:
                author = tag1.get_text().strip()
            elif tag2:
                author = "Editor: "+tag2.get_text().strip()
            else:
                author = "Unknown Author"

            tag = sourceDesc[0].findChild( name='pubplace' )
            if tag:
                pubPlace = tag.get_text().strip()
            else:
                pubPlace = "Unknown Publish Place"

            tag = sourceDesc[0].findChild( name='publisher' )
            if tag:
                publisher = tag.get_text().strip()
            else:
                publisher = "Unknown Publish Date"

            tag = sourceDesc[0].findChild( name='date' )
            if tag:
                date = tag.get_text().strip()
            else:
                date = "Unknown Publish Date"

            print allFilesInDirectory[x] + "    " + title + "   " + author +"   "+ pubPlace +"   "+ publisher +"   "+ date + "\n\n"

            totalsourceDescCount += 1
                    
            # insert into database
            insertCommand = "insert into SourceDesc values (?,?,?,?,?,?)"
            #print insertCommand
            try:
                cur.execute(insertCommand,(allFilesInDirectory[x],title,author,pubPlace,publisher,date))
            except sqlite3.Error,e:
                print "Failure to insert data.","\n",e.args[0]
                    
            db.commit()
                
print "TOTAl NUMBER OF FILES WITH ONE SOURCEDESC: " + str(totalsourceDescCount)
print "TOTAL NUMBER OF FILES WITH MORE THAN ONE SOURCEDESC: " + str(sourceDescerrorFileCount)
print "FILES WITHOUT SOURCEDESC: " + str(sourceDesclessFileCount),"\n\n"

# Select everyting from xml files in database---------------------------------------------------------------------------------

print "Which file do you want to read?" ,"\n","Please type the numbers of the files and then press Enter : " ,"\n"

# Show all filenames in database
selectFile = "SELECT distinct Filename FROM SourceDesc;"
cur.execute(selectFile)

FileNumber=0
FileList=[]
for filenames in cur:
    FileNumber+=1
    FileList.append(filenames[0])
    print str(FileNumber)+str(' ')+str(filenames),"\n"



# Read input from user

line = sys.stdin.readline()
line=line.split()

# Select everyting from the xml files that user want
for FileIndex in line:
    
    if (int(FileIndex)>0 and int(FileIndex)<FileNumber+1):
        TheFilename=FileList[int(FileIndex)-1]
        print str(TheFilename)
        selectCommand = "SELECT * FROM SourceDesc where Filename='"+str(TheFilename)+"';"
        cur.execute(selectCommand)
        k=0;
        for row in cur:
            k+=1;
            print row ,"\n"
        print "TOTAl NUMBER OF ROWS: " + str(k)+"\n"
    
    else:
        print "No such file number: " + str(FileIndex),"\n"

#Export from database into csv file
data = cur.execute( "SELECT * FROM SourceDesc;")

f = open('SourceDesc.csv', 'w')
print >> f, "Number in this file, Filename, Author, Epigraph, Hypertext Attributer, Atrribution Found"
for row in data:
    #row = unicode(row[0])+'@'+row[1]+'@'+row[2]+'@'+row[3]+'@'+row[4]
    print >> f, row
f.close()

db.close()
