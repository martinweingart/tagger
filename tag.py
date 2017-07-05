import eyed3
from datetime import datetime

#  eyed3.log.setLevel("ERROR")


class Tag():
    artist = unicode("")
    genre = unicode("")
    album = unicode("")
    title = unicode("")
    path = unicode("")
    track_num = 0
    recording_date = None
    v22 = False  # si tiene tag v2.2
    v23 = False  # si tiene tag v2.3
    v11 = False  # si tiene tag v1.1

    # FUNCION QUE CREA UN TAG GENERICO EN BASE A UN ARCHIVO mp3
    def create(self, archivo):
        print archivo
        self.path = archivo
        audioID3v2 = eyed3.core.load(archivo, (2, 3, 0))
        audioID3v1 = eyed3.core.load(archivo, (1, 1, 0))

        # Tiene un tag v2.x
        if (audioID3v2.tag is not None):
            # Tiene tag v2.2
            if (audioID3v2.tag.version == (2, 2, 0)):
                self.v22 = True
            # Tiene tag v2.3
            else:
                self.v23 = True
            self.artist = audioID3v2.tag.artist
            self.album = audioID3v2.tag.album
            self.title = audioID3v2.tag.title
            self.genre = audioID3v2.tag.genre
            self.track_num = audioID3v2.tag.track_num
            self.recording_date = audioID3v2.tag.recording_date

        # Tiene tag v1.1
        if (audioID3v1.tag is not None):
            self.v11 = True
            if (not(self.v23 or self.v22)):
                self.recording_date = audioID3v1.tag.release_date
                self.artist = audioID3v1.tag.artist
                self.album = audioID3v1.tag.album
                self.title = audioID3v1.tag.title
                self.genre = audioID3v1.tag.genre
                self.track_num = audioID3v1.tag.track_num

    # FUNCTION QUE ACTUALIZA O  CREA UN TAG EN EL ARCHIVO MP3
    def updateFile(self):
        audioID3v2 = eyed3.core.load(self.path, (2, 3, 0))
        if (not self.v23):  # si no tiene un tag v2.3
            audioID3v2.initTag()
        audioID3v2.tag.artist = self.artist
        audioID3v2.tag.album = self.album
        audioID3v2.tag.recording_date = self.recording_date
        audioID3v2.tag.title = self.title
        audioID3v2.tag.genre = self.genre
        audioID3v2.tag.track_num = self.track_num
        audioID3v2.tag.save()

    def setGenre(self, genre):
        self.genre = unicode(genre.decode('utf-8'))

    def setAlbum(self, album):
        self.album = unicode(album.decode('utf-8'))

    def setYear(self, year):
        self.recording_date = datetime(year, 1, 1)

    def setArtist(self, artist):
        self.artist = unicode(artist.decode('utf-8'))

    def setTrack(self, track):
        self.track = track

    def setTitle(self, title):
        self.title = unicode(title.decode('utf-8'))
