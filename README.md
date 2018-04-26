# BookOfBlackMagic
A compilation of misc. scripts I've written/use for my Plex system. Thought I may as well post them on github. Maybe someone else would find some of them useful as well. :)

# magicbullet.py
Currently just modifies plex server settings. However, it sets a hidden magical undocumented setting which forces all clients to use auto quality. Pretty much the closest/only option to set playback quality using the plex server :)

# The most amazing plex server setting you've never heard of: _forceAutoAdjustQuality_
forceAutoAdjustQuality - a super secret hidden plex server setting which will force clients to use auto quality for everything. It only activates when the client's set quality is less than the quality of the video. However, this is almost always true since the default quality of (almost?) every plex client is 2mbps.
## Examples:
- ex: quality set to 4mbps; watching >4mbps will trigger auto quality mode
- ex2: quality set to original/max; auto quality will never be used & you will always be streaming at the video's original bitrate

## **TL;DR: Force all clients / friends to use "Automatically adjust quality" when they are using the default settings (assuming it's a client which supports it)**
