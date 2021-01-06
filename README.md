# UPDATE 1-6-2021:
Check out my new work around using cloudflare workers here: https://github.com/zmike808/Plex-Blackmagic

# PSA REGARDING PLEX STEALTH NERF OF _forceAutoAdjustQuality_

Heads up to anyone still using this. forceAutoAdjustQuality has been countered by some really dark black magic. It 100% no longer works on plex.tv, which is really themost magical part. I went back to server version 1.13.8.5388 a month or 2 ago and I can confirm it will work on your direct domain such as plex.whyplexgottabelikethat.tears. But, like I said, that defeats the original purpose of this magical hidden setting, since it allowed friends you shared with to not have to herp derp at 2mbps default for their enitre lives. I have identified what is countering this magic however, I haven't had the time to deep dive into an attempted fix. It has to do with new headers being sent from plex.tv web clients. So, if anyone is interested in trying to fix it hit me up and I'd be willing to show you the evil headers in question. I have a general idea of how this may be fixable, but it would require having osme sort of middlelayer between plex.tv and the connection to the server maybe. I tried some basic things with nginx which yielded no results. 

TL;DR: Once again plex pulls a plex and dicks dedicated plex users for absolutely no reason. But for not my brethren, all hope has not been lost (yet)

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
