####################################################################################################
#	This plugin will find unmatched items for Plex Media Server
#
#	Made by dane22....A Plex Community member
#
#	Original python code was made by a Plex community member named whymse
#	and can be found here: 
#	http://forums.plexapp.com/index.php/topic/39712-list-unmatched-media/?p=252267
#	
#	The origen idea to the code belongs to whymse
#
#	I just made it a little bit more user friendly
#######
#
#	Remaking into just a script
#
####################################################################################################

import os
import unicodedata
import urllib2
import xml.etree.ElementTree as ET

####################################################################################################
# Skeleton
####################################################################################################
print("blahablahabla stuff about what it does")
print("You will need to enter your Plex Server Address. You can use either hostname or IP address")
print("Do not use any quotes or append the port number")
address = str(raw_input("Enter the address of your Plex Server now: "))

plexUrl = 'http://' + address + ':32400/library/sections'
url = plexUrl
tree = ET.parse(urllib2.urlopen(url))
root = tree.getroot()

for section in root:
	title = section.get("title")
	key = section.get("key")
	sectiontype = section.get("type")
	print title
	print sectiontype
	print key

##try:
##	myPathList[0][:] = []
##	myPathList[1][:] = []
##	sections = root.findall(".//Directory")
##	print sections
##	for section in sections:
##		title = section.get('title')
##		key = section.get('key')
##		sectiontype = section.get('type')
##		paths = section.xpath('Location path')
##		Log.Debug("Title of section is %s with a key of %s and a path of : %s" %(title, key, paths))
##		print title
##		print key
##		print sectiontype
##		print paths
###		for path in paths:
###			myPathList[0].append(key)
###			myPathList[1].append(path)
##except:
##	print("Exception")
##	pass






##def MainMenu():
##	Log.Debug("**********  Starting MainMenu  **********")
##	oc = ObjectContainer(no_cache=True)	
##	try:
##		#Clear our global varialble
##		myPathList[0][:] = []
##		myPathList[1][:] = []
##		sections = XML.ElementFromURL(PMS_URL).xpath('//Directory')	
##		for section in sections:			
##			title = section.get('title')
##			key = section.get('key')
##			sectiontype = section.get('type')
##			paths = section.xpath('Location/@path')				
##			Log.Debug("Title of section is %s with a key of %s and a path of : %s" %(title, key, paths))	
##			for path in paths:
##				# Need to append the key and path to a global variable, in order to avoid a bug in Plex API
##				myPathList[0].append(key)
##				myPathList[1].append(path)
##			oc.add(DirectoryObject(key=Callback(confirmScan, title=title, sectiontype=sectiontype, key=key), title='Look in section "' + title + '"'))	
##	except:
##		Log.Critical("Exception happend in MainMenu")
##		pass
##	oc.add(PrefsObject(title='Preferences', thumb=R('icon-prefs.png')))
##	Log.Debug("**********  Ending MainMenu  **********")
##	return oc
##
######################################################################################################
### Grab user selection of a section, and get to work
######################################################################################################
##@route(PREFIX + '/confirmScan')
##def confirmScan(title, key, sectiontype):
##	Log.Debug("*******  Starting confirmScan  ***********")
##	files = []
##
##	files[:] = []
##
##	Log.Debug("Section type is %s" %(sectiontype))
##
##	oc = ObjectContainer(title2="Search")
##	myMediaURL = PMS_URL + key + "/all"		
##	myMediaPaths = []
##	Log.Debug("Path to medias in section is %s" %(myMediaURL))
##	# Scan the database based on the type of section
##	if sectiontype == "movie":
##		myMediaPaths = scanMovieDB(myMediaURL)
##	if sectiontype == "show":
##		myMediaPaths = scanShowDB(myMediaURL)
##	if sectiontype == "artist":
##		myMediaPaths = scanArtistDB(myMediaURL)
##
##
##
##	Log.Debug("Section filepath as stored in the database are: %s" %(myMediaPaths))
##	# Now we need all filepaths added to the section
##	for i, j in enumerate(myPathList[0]):
##    		if j == key:
##			# Scan the filesystem
##			files.append(listTree(myPathList[1][i]))
##	Log.Debug("Files found are the following:")
##	Log.Debug(files)
##	missing = findUnmatchedFiles(files, myMediaPaths)
##	Log.Info("*********************** The END RESULT Start *****************")
##	Log.Info("The following files are missing in Plex database from section named: %s:" %(title))
##	if 0 == len(missing):
##		missing.append("All is good....no files are missing")
##	Log.Info(missing)
##	print(missing)
##	Log.Info("*********************** The END RESULT End *****************")
##	Log.Debug("*******  Ending confirmScan  ***********")
##	oc2 = ObjectContainer(title1="Unmatched Items found", mixed_parents=True)
##	for missed in missing:
##		oc2.add(DirectoryObject(key=Callback(confirmScan), title=missed))
##	return oc2
##
######################################################################################################
### Do the files
######################################################################################################
##@route(PREFIX + '/findUnmatchedFiles')
##def findUnmatchedFiles(filePaths, dbPaths):
##	missing = []
##	fname = ""
##	display_ignores = False
##
##	Log.Debug("******* Start findUnmatchedFiles ******")
##	Log.Debug("***********************************************************************************")
##	Log.Debug("Database paths:")
##	Log.Debug(dbPaths)
##	Log.Debug("***********************************************************************************")
##	for myFiles in filePaths:
##		Log.Debug("myFile is %s" %(myFiles))
##		for filePath in myFiles:
##			Log.Debug("Handling file %s ..." %(filePath))		
##			if filePath not in dbPaths:
##				Log.Debug(filePath)
##				myext = os.path.splitext(filePath)[1].lower()
##				cext = myext.rstrip("']")
##				fname = os.path.split(filePath)[1]
##				Log.Debug("filepath was not in paths, so fname is now %s" %(fname))
##				Log.Debug("file ext is : %s" %(cext))
##				if (fname in OK_FILES):
##					#Don't do anything for acceptable files
##					Log.Debug("File is part of OK_Files")
##					continue
##				elif (cext in OTHER_EXTENSIONS):
##					#ignore images and subtitles
##					Log.Debug("File is part of ignored extentions")
##					continue
##				elif (cext not in VALID_EXTENSIONS):
##					#these shouldn't be here
##					if (display_ignores):
##						Log.Debug("Ignoring %s" %(filePath))
##						continue
##				else:
##					Log.Debug("Missing this file")
##					missing.append(filePath)
##	return missing
##
######################################################################################################
### Get user settings, and if not existing, get the defaults
######################################################################################################
##@route(PREFIX + '/getPrefs')
##def getPrefs():
##	Log.Debug("*********  Starting to get User Prefs  ***************")
##	global host
##	host = Prefs['host']
##	if host.find(':') == -1:
##		host += ':32400'
##	global PMS_URL
##	PMS_URL = 'http://%s/library/sections/' %(host)
##	Log.Debug("PMS_URL is : %s" %(PMS_URL))
##	global VALID_EXTENSIONS
##	VALID_EXTENSIONS = Prefs['VALID_EXTENSIONS']
##	Log.Debug("VALID_EXTENSIONS from prefs are : %s" %(VALID_EXTENSIONS))	
##	global OK_FILES
##	OK_FILES = Prefs['OK_FILES']
##	Log.Debug("OK_FILES from prefs are : %s" %(OK_FILES))
##	global IGNORED_DIRS
##	IGNORED_DIRS = Prefs['IGNORED_DIRS']
##	Log.Debug("IGNORED_DIRS from prefs are : %s" %(IGNORED_DIRS))
##	global OTHER_EXTENSIONS
##	OTHER_EXTENSIONS = Prefs['OTHER_EXTENSIONS']
##	Log.Debug("OTHER_EXTENSIONS from prefs are : %s" %(OTHER_EXTENSIONS))
##	Log.Debug("*********  Ending get User Prefs  ***************")
##	return
##
######################################################################################################
### This function will scan the filesystem for files
######################################################################################################
##@route(PREFIX + '/listTree')
##def listTree(top, files=list()):
##	Log.Debug("******* Starting ListTree with a path of %s***********" %(top))
##	r = files[:]
##	try:
##		if not os.path.exists(top):
##			Log.Debug("The file share [%s] is not mounted" %(top))
##			return r
##		for f in os.listdir(top):
##			pathname = os.path.join(top, f)
##			Log.Debug("Found a file named : %s" %(pathname))
##			if os.path.isdir(pathname):
##				r = listTree(pathname, r)
##			elif os.path.isfile(pathname):
###				r.append(unicodedata.normalize('NFC', pathname))
##				r.append(pathname)
##			else:
##				Log.Debug("Skipping %s" %(pathname))
##		return r
##	except UnicodeDecodeError:
##		Log.Critical("Detected an invalid caracter in the file/directory following this : %s" %(pathname))
##
######################################################################################################
### This function will scan a movie section for filepaths in medias
######################################################################################################
##@route(PREFIX + '/scanMovieDB')
##def scanMovieDB(myMediaURL, myMediaPaths=list()):
##	Log.Debug("******* Starting scanMovieDB with an URL of %s***********" %(myMediaURL))
##	r = myMediaPaths[:]
##	try:
##		myMedias = XML.ElementFromURL(myMediaURL).xpath('//Video')
##		for myMedia in myMedias:
##			title = myMedia.get('title')
##			myFilePath = str(myMedia.xpath('Media/Part/@file'))[2:-2]
##			myMediaPaths.append(myFilePath)
##			Log.Debug("Media from database: '%s' with a path of : %s" %(title, myFilePath))
##			r.append(myFilePath)
##		return r
##	except:
##		Log.Critical("Detected an exception in scanMovieDB")
##		pass
##
##
######################################################################################################
### This function will scan a TV-Show section for filepaths in medias
######################################################################################################
##@route(PREFIX + '/scanShowDB')
##def scanShowDB(myMediaURL, myMediaPaths=list()):
##	Log.Debug("******* Starting scanShowDB with an URL of %s***********" %(myMediaURL))
##	r = myMediaPaths[:]
##	Log.Debug("Host is %s" %(host))
##	try:
##		myMedias = XML.ElementFromURL(myMediaURL).xpath('//Directory')
##		for myMedia in myMedias:
##			ratingKey = myMedia.get("ratingKey")
##			Log.Debug("RatingKey is %s" %(ratingKey))
##			myURL = "http://" + host + "/library/metadata/" + ratingKey + "/allLeaves"
##			Log.Debug("myURL is %s" %(myURL))
##			myMedias2 = XML.ElementFromURL(myURL).xpath('//Video')
##			for myMedia2 in myMedias2:
##				title = myMedia2.get("grandparentTitle") + "/" + myMedia2.get("title")
##				myFilePath = myMedia2.xpath('Media/Part/@file')
##				for myFilePath2 in myFilePath:
##					myMediaPaths.append(myFilePath2)					
##					Log.Debug("Media from database: '%s' with a path of : %s" %(title, myFilePath2))
##					r.append(myFilePath2)
##		return r
##	except:
##		Log.Critical("Detected an exception in scanShowDB")
##		pass
##	Log.Debug("******* Ending scanShowDB ***********")
##
##
######################################################################################################
### This function will scan a Music section for filepaths in medias
######################################################################################################
##@route(PREFIX + '/scanArtistDB')
##def scanArtistDB(myMediaURL, myMediaPaths=list()):
##	Log.Debug("******* Starting scanArtistDB with an URL of %s***********" %(myMediaURL))
##	r = myMediaPaths[:]
##	Log.Debug("Host is %s" %(host))
##	try:
##		myMedias = XML.ElementFromURL(myMediaURL).xpath('//Directory')
##		for myMedia in myMedias:
##			ratingKey = myMedia.get("ratingKey")
##			Log.Debug("RatingKey is %s" %(ratingKey))
##			myURL = "http://" + host + "/library/metadata/" + ratingKey + "/allLeaves"
##			Log.Debug("myURL is %s" %(myURL))
##			myMedias2 = XML.ElementFromURL(myURL).xpath('//Track')
##			for myMedia2 in myMedias2:
##				title = myMedia2.get("grandparentTitle") + "/" + myMedia2.get("title")
##				myFilePath = str(myMedia2.xpath('Media/Part/@file'))[2:-2]
##				myMediaPaths.append(myFilePath)
##				Log.Debug("Media from database: '%s' with a path of : %s" %(title, myFilePath))
##				r.append(myFilePath)
##		return r
##	except:
##		Log.Critical("Detected an exception in scanArtistDB")
##		pass
##	Log.Debug("******* Ending scanArtistDB ***********")
