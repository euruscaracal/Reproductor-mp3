import eyed3
import os
class minero:


    def __init__(self):
        self.listasa = []
        '/home/rominacaracal/Escritorio/Reproductor/testFiles/Music'
        self.listad = os.walk('/home/rominacaracal/Escritorio/Reproductor/testFiles/Music')

    def crea(self):
        nuevaruta = r'ruta/al/directorio/directorio'
        if not os.path.exists(nuevaruta): os.makedirs(nuevaruta)

    #existe un directorio
    def existeDirectorio(self):
        try:
           f = open("foo.txt")
        except IOError as e:
           print("Uh oh! Esto no existe")

    def identifyMp3(self):
        for root, dirs, files in self.listad:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".mp3"):
                    self.listasa.append(nombreFichero+extension)
        return self.listasa

    def getTags(self):

        o = self.identifyMp3()
        for i in o:
            song = eyed3.load('/home/rominacaracal/Escritorio/Reproductor/testFiles/Music/' + i)
            print('Titulo: ', song.tag.title)
            print('Artist: ', song.tag.artist)
            print('Year: ' , song.tag.release_date)
            print('Track: ' , song.tag.track_num)
            print('Genre: ' , song.tag.genre)


m = minero()
m.crea()
m.identifyMp3()
m.getTags()
