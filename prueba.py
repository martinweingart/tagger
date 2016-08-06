from os import walk
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()

for root, dirs, files in os.walk(args.folder):
    for file in files:
        name, ext = os.path.splitext(file)
        if not (ext in ['.mpc','.png','.PNG','.ini', '.mp3', '.jpg', '.JPG', '.db', '.jpeg', '.MP3', '.Mp3']):
            print os.path.join(root, file)
            x = raw_input("seguir...")
            os.remove(os.path.join(root, file))
