import os
import unicodedata
import sys
import re


## open log file after scan##
## Find OS type to find Plex Unmatched media log##
os_set = sys.platform
pathtoLog = ''

##while True:
##        manualCheck = str(raw_input("Did you want to manually load log file location? (y/n)"))
##        if manualCheck == ('y'|'Y'):
##                logPath = raw_input("Enter path to log without quotes:")
##                break
##        else:
##if (os_set == 'linux2'):
##        pathtoLog = '/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.plexapp.plugins.findUnmatch.log'
####                        break
##elif (os_set == 'win32'):
##        Userwin32 = os.environ['USERPROFILE']
##        pathtoLog = Userwin32+'\\AppData\\Local\\Plex Media Server\\Logs\\PMS Plugin Logs\\com.plexapp.plugins.findUnmatch.log'
####                        break
##elif (os_set == 'darwin'):
##        pathtoLog = '~/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.plexapp.plugins.findUnmatch.log'
####                        break
##else:
##        print "Error setting path to database on your operating system!!"
####                        break


####EDIT ME##
## Example below
results = open("C:\Users\david.bell\Documents\GitHub\Plex-FindUnmatched-Script\com.plexapp.plugins.findUnmatch.txt")
##results = open('/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.plexapp.plugins.findUnmatch.log')


##logPath = os.path.expanduser(pathtoLog)
##results = open(logPath)


##test dir
##results = open("C:\Users\USER\Documents\GitHub\Plex-FindUnmatched-Script\com.plexapp.plugins.findUnmatch.txt")

resultsLine = results.readlines()


lookup = "The END RESULT Start"
missingLine = []
missingFound = []

def genHtml(missing):
        userFilePath = os.path.expanduser('~')
        missingFile = open(userFilePath+"MissingFiles.html", "w")
        m = missing[:]
        try:
                missingFile.write("<!DOCTYPE html>\n<html>\n<body>\n<h1>Missing items</h1>")
                for item in m:
                        missingFile.write("<p>"+item.decode('utf-8')+"</p>")


                missingFile.write("\n</body>\n</html>")
        except:
                pass


##Find next list line'missing' output ##
foundLine = False

##Iterate file for lines##
for num, items in enumerate(resultsLine):
        items = items.rstrip()
        if lookup in items:
##Found line now grab the line 2 down (has the list)##
##Still need to confirm the front half is always 65##               
                for i in range(1):
                        nextLine = num + 2
                        missingItem = resultsLine[nextLine]
                        missingItem = missingItem[65:]
                        missingLine = re.split('\', \'|\", \"|\', \"|\", \'', missingItem)
        
genHtml(missingLine)
