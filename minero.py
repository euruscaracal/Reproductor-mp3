import os

class mp3:

    def __init__(self):
        self.i = 0

    def crea(self):
        nuevaruta = r'ruta/al/directorio/directorio'
        if not os.path.exists(nuevaruta): os.makedirs(nuevaruta)

    #recorrer directorio
    def busca(self):
        rootDir = ''
        for dirName, subdirList, fileList in os.walk(rootDir):
            print('Directorio encontrado: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)

    #existe un directorio
    def existedirectorio(self):
        try:
           f = open("foo.txt")
        except IOError as e:
           print("Uh oh! Esto no existe")

k = mp3()
k.crea()
k.busca()
k.existedirectorio()
