from mutagen.id3 import ID3, TIT2, \
                        TDRC, TRCK, \
                        TPE1, TALB, TCON


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
        audio = ID3(self.path)
        self.artist = unicode(audio.get('TPE1'))
        self.album = unicode(audio.get('TALB'))
        self.title = unicode(audio.get('TIT2'))
        self.genre = unicode(audio.get('TCON'))
        self.track = unicode(audio.get('TRCK'))
        self.year = unicode(audio.get('TDRC'))

    # FUNCTION QUE ACTUALIZA O  CREA UN TAG EN EL ARCHIVO MP3
    def updateFile(self):
        audio = ID3(self.path)
        audio.add(TPE1(encoding=3, text=self.artist))
        audio.add(TALB(encoding=3, text=self.album))
        audio.add(TDRC(encoding=3, text=self.year))
        audio.add(TIT2(encoding=3, text=self.title))
        audio.add(TCON(encoding=3, text=self.genre))
        audio.add(TRCK(encoding=3, text=self.track))
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
