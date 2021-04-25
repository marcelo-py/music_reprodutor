import os
from pygame import mixer


class MusicPlayer:
    def __init__(self):
        self.musicas_diretorio = list()


    def buscar_no_diretorio(self, diretorio):
        self.diretorio = diretorio
        for raiz, diretorio, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if arquivo[-4:] == '.mp3':
                    self.musicas_diretorio.append(arquivo)

class Usuario:
    def __init__(self, classe_musica):
        self.musicas = classe_musica
        self.musicas_achadas = []

    def mostrar(self):
        for i, musica in enumerate(self.musicas.musicas_diretorio):
            print('{}- {}'.format(i, musica))

    def procurar(self, palavra):

        for musicas in self.musicas.musicas_diretorio:
            if palavra.lower() in musicas.lower():
                self.musicas_achadas.append(musicas)

        if len(self.musicas_achadas) >= 1:
            for n, achado in enumerate(self.musicas_achadas):
                print('{}- {}'.format(n,achado))
        else:
            print('Nenhuma música encontrada! :(')

    def reproduzir(self, msg):
        ok = False
        numero = ()
        while True:
            n = input(msg)
            if n.isnumeric():
                numero = int(n)
                ok = True
            else:
                print('Digite um numero inteiro valido!')

            if ok:
                break

        mixer.init()
        if len(self.musicas_achadas) > 0:

            mixer.music.load(self.musicas.diretorio+'/'+self.musicas_achadas[numero])

        elif len(self.musicas_achadas) == len(self.musicas.musicas_diretorio):
            mixer.music.load(self.musicas.diretorio + '/' + self.musicas.musicas_diretorio[numero])

        elif numero > len(self.musicas_achadas) and numero <= len(self.musicas.musicas_diretorio):
            mixer.music.load(self.musicas.diretorio + '/' + self.musicas.musicas_diretorio[numero])

        else:
            print('Opção invalida')

        mixer.music.play()
        while mixer.music.get_busy(): pass


    def voltar(self):
        self.musicas_achadas.clear()


#main test
a = MusicPlayer()
u = Usuario(a)
a.buscar_no_diretorio(r'diretorio') #esse metodo recebe o diretorio onde o usuario quer pegar as musicas

procurar = input('Digite uma palavra para pesquisar')

u.procurar(procurar)
#u.voltar()
#u.mostrar()
u.reproduzir('Digite o numero que quer reproduzir')

