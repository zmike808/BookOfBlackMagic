#!/usr/bin/env python3

# WARNING: this is a script I threw together and wasn't planning to share with people; so the code quality / documentation is pretty shit.
# forceAutoAdjustQuality - some super secret hidden plex server API setting which will force clients to use auto quality for everything
# unless they have a quality set higher than the quality of the video in question
# (ex: quality set to 4mbps; watching >4mbps will trigger auto quality mode)
# ex2: quality set to original/max; auto quality will never be used & you will always be streaming at the video's original bitrate
# TL;DR: clients won't default to transcoding at 2mbps anymore (srsly plex why would that be the default in the first place?)

#REQUIRES PLEXAPI: pip install plexapi (http://python-plexapi.readthedocs.io/en/latest/introduction.html)

from plexapi.myplex import MyPlexAccount, PlexServer

# Maybe one of these days I'll switch to YAML file for credentials like a good coder ;)
username = 'SERVER_OWNER_USERNAME_HERE'
password = 'REPLACE_ME'
servername = 'Friendly_name' #Friendly name (the name you set in general settings for your server)

# set to directly connect to plex server without going through plex account auth
baseurl = 'http://plexserver:32400' #use if you have a custom plex URL defined
token = 'PLEX_SERVER_TOKEN'

# server settings to change
# you can probably just manually add these into Preferences.xml instead of using this script but oh well?
settings_dict = {
    'forceAutoAdjustQuality':True,
    'allowHighOutputBitrates':True,
} #Some srsly undocumented blackmagic.


def get_plex_server():
    #don't try this at home kids. this is how you become a bad coder.
    try:
        # try using user/pass/server name first
        return MyPlexAccount(username, password).resource(servername).connect()
    except:
        # fall back to using url/token to connect to server
        return PlexServer(baseurl, token)

    # Should never get here because that would mean you never changed any of the default credentials...
    # And who would be that silly? :)
    raise Exception("You had one job. One. Job.")

def main():
    plex = get_plex_server()
    pset = plex.settings

    for x,y in settings_dict.items():
        s = plex.settings.get(x)
        print(s)
        print('current value for {0}: {1}'.format(x, s.value))
        s.set(y)
        plex.settings.save()

    # get fresh server instance because reasons
    confirm = get_plex_server()  # returns a PlexServer instance
    for x,y in settings_dict.items():
        s = confirm.settings.get(x)
        print('{} -- expected: {} -- actual: {}'.format(x, y, s.value))

if __name__ == "__main__":
    main()