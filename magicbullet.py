#!/usr/bin/env python3

# WARNING: this is a script I threw together and wasn't planning to share with people; so the code quality / documentation is pretty shit.
# forceAutoAdjustQuality - some super secret hidden plex server API setting which will force clients to use auto quality for everything
# unless they have a quality set higher than the quality of the video in question
# (ex: quality set to 4mbps; watching >4mbps will trigger auto quality mode)
# ex2: quality set to original/max; auto quality will never be used & you will always be streaming at the video's original bitrate
# TL;DR: clients won't default to transcoding at 2mbps anymore (srsly plex why would that be the default in the first place?)

#REQUIRES PLEXAPI: pip install plexapi (http://python-plexapi.readthedocs.io/en/latest/introduction.html)

from plexapi.myplex import MyPlexAccount

username = 'SERVER_OWNER_USERNAME_HERE'
password = 'REPLACE_ME'
servername = 'Friendly_name' #Friendly name (the name you set in general settings for your server)
account = MyPlexAccount(username, password)
plex = account.resource(servername).connect()  # returns a PlexServer instance
pset = plex.settings
print(pset.all())

setlist = ['forceAutoAdjustQuality'] #Some srsly undocumented blackmagic.
for x in setlist:
    s = plex.settings.get(x)
    plex.settings.get(x).set(True)
    s._setValue = 'true'
    s.value = True
    plex.settings.save()
    print(plex.settings.get(x), plex.settings.get(x).value, plex.settings.get(x)._setValue)

print(plex.settings.all())