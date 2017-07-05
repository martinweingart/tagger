# !/home/mweingart/Proyectos/tagger/local/bin/python
#  -*- coding: utf-8 -*-

#  IMPORTS
import os.path
from tag import Tag
import argparse


def isMP3(filePath):
    fileName, fileExt = os.path.splitext(filePath)
    return fileExt == '.mp3' or fileExt == '.MP3'


# Arguments handler
def argHandler():
    parser = argparse.ArgumentParser()
    inputArgGroup = parser.add_mutually_exclusive_group()
    inputArgGroup.add_argument(
        "-f",
        "--file",
        help="Update tag of given mp3 file"
    )

    inputArgGroup.add_argument(
        "-r",
        "--recursively",
        help="Update tag recursively on the specified folder"
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


def updateFolder(folder, args):
    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            if (isMP3(file)):
                tag = Tag()
                tag.create(os.path.join(root, file))
                updateTag(tag, args)
                tag.updateFile()


# Main Function
# es una carpeta y existe
def main():
    args = argHandler()
    if args.recursively is None:
        if (args.file is None):
            print "Error: Must especified at least one argument: -f (file)" \
                  + " or -r (folder)"
        else:
            if (checkPath(args.file, 'File')):
                if (isMP3(args.file)):
                    tag = Tag()
                    tag.create(args.file)
                    updateTag(tag, args)
                    tag.updateFile()
                else:
                    print "Error: is not mp3 file"
    else:
        if (checkPath(args.recursively, 'Folder')):
            for root, dirs, files in os.walk(args.recursively, topdown=False):
                for file in files:
                    if (isMP3(file)):
                        tag = Tag()
                        tag.create(os.path.join(root, file))
                        updateTag(tag, args)
                        tag.updateFile()
    print "Done!"


#  Ejecuto el script
if __name__ == "__main__":
    main()
