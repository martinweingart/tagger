from os import path


def isMP3(file):
    fileName, fileExt = path.splitext(file)
    return fileExt == '.mp3' or fileExt == '.MP3'


def isWMA(file):
    fileName, fileExt = path.splitext(file)
    return fileExt == '.wma' or fileExt == '.WMA'


def isAudioFile(file):
    return isMP3(file) or isWMA(file)
