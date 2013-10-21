import os
import unicodedata
import sys

## open log file after scan##
results = open("/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Logs/PMS\ Plugin\ Logs/com$
lookup = "*********************** The END RESULT Start *****************"
missingLine = ""

##Find line number for 'missing' output ##
with results as file:
        for num, line in enumerate(file, 1):
                if lookup in line:
                        missingLine = num

## Thinking putting a str tag on the actual line may make it easier later
## Shouldnt affect the plugin

## Find line index (still would need to split the rest of the line and pass that into genHtml
#startParse = string.rfind("MissingTag")


def genHtml(missing):
        userFilePath = os.path.expanduser('~')
        missingFile = open(userFilePath+"/MissingFiles.html", "w")
        Log.Debug("******* Starting Export of %s***********" %(missingFile))
        m = missing[:]
        try:
                missingFile.write("<!DOCTYPE html>\n<html>\n<body>\n<h1>Missing items</h1>"
                for item in m:
                        missingFile.write("<p>"+item+"</p>")

                missingFile.write("\n</body>\n</html>")
        except:
                Log.Critical("There was an issue generating HTML")
                pass
