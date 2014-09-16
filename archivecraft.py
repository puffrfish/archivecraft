import urllib
import urllib2
import json
import os

req = urllib2.Request("http://s3.amazonaws.com/Minecraft.Download/versions/versions.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.loads(f.read())

if not os.path.exists("archivecraft"):
	os.mkdir("archivecraft")
	print "Created archivecraft directory"

if not os.path.exists("archivecraft/client"):
	os.mkdir("archivecraft/client")
	print "Created archivecraft/client directory"

if not os.path.exists("archivecraft/server"):
	os.mkdir("archivecraft/server")
	print "Created archivecraft/server directory"

for i in data['versions']:
	if not os.path.exists("archivecraft/client/%s" % (i['type'])):
		os.mkdir("archivecraft/client/%s" % (i['type']))
		print "Created archivecraft/client/%s directory" % (i['type'])

for i in data['versions']:
	if not os.path.exists("archivecraft/server/%s" % (i['type'])):
		os.mkdir("archivecraft/server/%s" % (i['type']))
		print "Created archivecraft/server/%s directory" % (i['type'])

print "\n"

for i in data['versions']:
	print "Downloading client %s %s" % (i['type'], i['id'])
	urllib.urlretrieve("http://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.jar" % (i['id'], i['id']), "archivecraft/client/%s/%s.jar" % (i['type'], i['id']))
	print "Downloading server %s %s" % (i['type'], i['id'])
	urllib.urlretrieve("http://s3.amazonaws.com/Minecraft.Download/versions/%s/minecraft_server.%s.jar" % (i['id'], i['id']), "archivecraft/server/%s/minecraft_server.%s.jar" % (i['type'], i['id']))
	print "\n"
