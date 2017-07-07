# !/home/mweingart/Proyectos/tagger/local/bin/python
#  -*- coding: utf-8 -*-

#  IMPORTS
import os
from tag import Tag
import argparse
import utils


# Arguments handler
def argHandler():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target",
        help="Target file or directory to update"
    )

    parser.add_argument(
        "-r",
        "--recursively",
        help="Update tag recursively on the specified folder",
        action="store_true"
    )

    parser.add_argument(
        "-g",
        "--genre",
        help="Update genre in tag of given mp3 file or folder"
    )

    parser.add_argument(
        "-a",
        "--artist",
        help="Update artist in tag of given mp3 file or folder"
    )

    parser.add_argument(
        "-b",
        "--album",
        help="Update album in tag of given mp3 file or folder"
    )

    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="Update year in tag of given mp3 file or folder. Must be integer"
    )

    parser.add_argument(
        "-t",
        "--title",
        help="Update title in tag of given mp3 file or folder"
    )

    parser.add_argument(
        "-n",
        "--track",
        help="Update track num in tag of given mp3 file or folder"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="ver detalles de acciones",
        action="store_true"
    )
    args = parser.parse_args()
    return args


# Functions
def checkPath(path, type):
    if (not os.path.exists(path)):
        print type, "not found"
        return False
    else:
        return True


def updateTag(tag, args):
    if (args.verbose):
        print "Updating tag from file", tag.path, "..."
    if (args.genre):
        tag.setGenre(args.genre)
    if (args.title):
        tag.setTitle(args.title)
    if (args.artist):
        tag.setArtist(args.artist)
    if (args.album):
        tag.setAlbum(args.album)
    if (args.year):
        tag.setYear(args.year)
    if (args.track):
        tag.setTrack(args.track)


def main():
    args = argHandler()
    if (not os.path.exists(args.target)):
        print "File (or folder) not found"
    else:
        if os.path.isfile(args.target):
            if utils.isAudioFile(args.file):
                tag = Tag()
                tag.create(args.file)
                updateTag(tag, args)
                tag.updateFile()
            else:
                print "Error: is not a audio file"
        else:
            if (args.recursively):
                for root, dirs, files in os.walk(args.target, topdown=False):
                    for file in files:
                        if utils.isAudioFile(file):
                            tag = Tag()
                            tag.create(os.path.join(root, file))
                            updateTag(tag, args)
                            tag.updateFile()
            else:
                for elem in os.listdir(args.target):
                    if os.path.isfile(elem):
                        tag = Tag()
                        tag.create(os.path.join(args.target, elem))
                        updateTag(tag, args)
                        tag.updateFile()
    print "Done!"


#  Ejecuto el script
if __name__ == "__main__":
    main()
