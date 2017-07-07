from mutagen.id3 import ID3, TIT2, \
                        TDRC, TRCK, \
                        TPE1, TALB, TCON
from mutagen.asf import ASF

import utils


class Tag():
    artist = u""
    genre = u""
    album = u""
    title = u""
    path = u""
    track = u""
    year = u""

    # FUNCION QUE CREA UN TAG GENERICO EN BASE A UN ARCHIVO mp3
    def create(self, archivo):
        self.path = archivo
        if utils.isMP3(archivo):
            audio = ID3(self.path)
            self.artist = unicode(audio.get('TPE1'))
            self.album = unicode(audio.get('TALB'))
            self.title = unicode(audio.get('TIT2'))
            self.genre = unicode(audio.get('TCON'))
            self.track = unicode(audio.get('TRCK'))
            self.year = unicode(audio.get('TDRC'))
        elif utils.isWMA(archivo):
            audio = ASF(self.path)
            self.artist = unicode(audio.get('Author')[0]) if audio.get('Author') else ''
            self.album = unicode(audio.get('WM/AlbumTitle')[0]) if audio.get('WM/AlbumTitle') else ''
            self.title = unicode(audio.get('Title')[0]) if audio.get('Title') else ''
            self.genre = unicode(audio.get('WM/Genre')[0]) if audio.get('WM/Genre') else ''
            self.track = unicode(audio.get('WM/TrackNumber')[0]) if audio.get('WM/TrackNumber') else ''
            self.year = unicode(audio.get('WM/OriginalReleaseYear')[0]) if audio.get('WM/OriginalReleaseYear') else ''

    # FUNCTION QUE ACTUALIZA O  CREA UN TAG EN EL ARCHIVO MP3
    def updateFile(self):
        if utils.isMP3(self.path):
            audio = ID3(self.path)
            audio.add(TPE1(encoding=3, text=self.artist))
            audio.add(TALB(encoding=3, text=self.album))
            audio.add(TDRC(encoding=3, text=self.year))
            audio.add(TIT2(encoding=3, text=self.title))
            audio.add(TCON(encoding=3, text=self.genre))
            audio.add(TRCK(encoding=3, text=self.track))
        elif utils.isWMA(self.path):
            audio = ASF(self.path)
            audio['Title'] = self.title
            audio['Author'] = self.artist
            audio['WM/AlbumTitle'] = self.album
            audio['WM/Genre'] = self.genre
            audio['WM/TrackNumber'] = self.track
            audio['WM/OriginalReleaseYear'] = self.year
        else:
            print self.path
        audio.save()

    def setGenre(self, genre):
        self.genre = unicode(genre.decode('utf-8'))

    def setAlbum(self, album):
        self.album = unicode(album.decode('utf-8'))

    def setYear(self, year):
        self.year = str(year)

    def setArtist(self, artist):
        self.artist = unicode(artist.decode('utf-8'))

    def setTrack(self, track):
        self.track = track

    def setTitle(self, title):
        self.title = unicode(title.decode('utf-8'))
