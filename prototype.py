#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pytube import Playlist

play_list = Playlist("https://www.youtube.com/playlist?list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10")
print(len(play_list))

for link in play_list:
    print(link)
for video in play_list.videos:
    name = video.title
    print(name)
