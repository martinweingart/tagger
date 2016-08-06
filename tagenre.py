# -*- coding: utf-8 -*-

import eyed3
from os import listdir, walk
import os
import sys
from tagger import updateFolder
import argparse
from argparse import Namespace


eyed3.log.setLevel("ERROR")


parser = argparse.ArgumentParser()
parser.add_argument('band',
                    help='Band where to start')
args = parser.parse_args()

band = args.band
show = False

for folder in listdir('/media/tincho/Martin/Música/Discos'):
    if (band == folder or show):
        show = True
        print "show:", folder;
        try:
            change = raw_input("Change? y/n")
        except KeyboardInterrupt:
            exit()
        else:
            if (change=='y'):
                try:
                    genre = raw_input("Genre:")
                    names = Namespace(album=None, artist=None, file=None, genre=genre, recursively=None, title=None, track=None, year=None)
                    updateFolder('/media/tincho/Martin/Música/Discos/' + folder, names)
                except KeyboardInterrupt:
                    exit()
