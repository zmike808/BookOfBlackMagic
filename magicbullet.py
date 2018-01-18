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
#print(pset.all())

settings_dict = {
    'forceAutoAdjustQuality':True,
    'enableAirplay':True,
    'allowHighOutputBitrates':True,
    'segmentedTranscoderTimeout':120
} #Some srsly undocumented blackmagic.
for x,y in settings_dict.items():
    s = plex.settings.get(x)
    print(s)
    print('current value for {0}: {1}'.format(x, s.value))
    s.set(y)
    # s._setValue = 'true'
    # s.value = True
    plex.settings.save()

confirm = account.resource(servername).connect()  # returns a PlexServer instance
for x,y in settings_dict.items():
    s = confirm.settings.get(x)
    print('expected: {}; actual: {}'.format(y, s.value))
