import os
import unicodedata
import sys
import csv

## open log file after scan##
#results = open("/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Logs/PMS\ Plugin\ Logs/com$

##test dir
results = open("C:\Users\david.bell\Documents\GitHub\Plex-FindUnmatched-Script\com.plexapp.plugins.findUnmatch.txt")
resultsLine = results.readlines()

lookup = "The END RESULT Start"
missingLine = []

##def genHtml(missing):
##        userFilePath = os.path.expanduser('~')
##        missingFile = open(userFilePath+"/MissingFiles.html", "w")
####        Log.Debug("******* Starting Export of %s***********" %(missingFile))
##        m = missing[:]
##        try:
##                missingFile.write("<!DOCTYPE html>\n<html>\n<body>\n<h1>Missing items</h1>")
##                for item in m:
##                        missingFile.write("<p>"+item+"</p>")
##
##                missingFile.write("\n</body>\n</html>")
##        except:
####                Log.Critical("There was an issue generating HTML")
##                pass
##
##Find line number for 'missing' output ##
foundLine = False

for num, items in enumerate(resultsLine, 0):
##        items = items.rstrip()
        if lookup in items:
##                for i in range(1):
                nextLine = num + 2
##                        print resultsLine[nextLine]
                missingItem = resultsLine[nextLine]
                missingLine.append(missingItem)
##                print items
##                print missingLine

print str(missingLine[0])

##genHtml(missingLine[2])

##with results as file:
##        for num, line in enumerate(file, 0):
##                line = line.rstrip()
##                if lookup in line:
##                        foundLine = True
##                        if foundLine:
##                                a = 0
##                                while a < 5:
##                                        a = a + 1
##                        missingLine.append(line)
##                       ## print(line)
##                        print(missingLine)

## Thinking putting a str tag on the actual line may make it easier later
## Shouldnt affect the plugin

## Find line index (still would need to split the rest of the line and pass that into genHtml
#startParse = string.rfind("MissingTag")
