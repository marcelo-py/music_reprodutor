import os
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        self.musicas_diretorio = list()


    def buscar_no_diretorio(self, diretorio):
        self.diretorio = diretorio
        try:
            for raiz, diretorio, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    if arquivo[-4:] == '.mp3':
                        self.musicas_diretorio.append(arquivo)
        except Exception:
            print('Erro desconhecido! tente ver se esta tudo certo com o diretorio! ')

    def tela(self, opção):
        while True:
            opç = input()

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
        try:
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
            cont = 0

            while mixer.music.get_busy():
                print()
                if cont == 0 and len(self.musicas_achadas) >= 1:
                    print('Tocando agora... {}'.format(self.musicas_achadas[numero]))
                    cont += 1

                t = input('[P]Pause||  [R]Retomar↻   [S]Stop▣ ').lower()


                if t == 'p':
                    mixer.music.pause()
                    print('Música pausada!')

                elif t == 'r':
                    mixer.music.unpause()
                    print('Música retomada!')
                    print('Tocando... {}'.format(self.musicas_achadas[numero]))


                elif t == 's':
                    mixer.music.stop()

        except Exception:
               print('Erro! Talvez não há nada na pasta ou esta é uma opção inválida')


    def voltar(self):
        self.musicas_achadas.clear()

#main test
a = MusicPlayer()
u = Usuario(a)
a.buscar_no_diretorio(r'diretorio completo...') #esse metodo recebe o diretorio onde o usuario quer pegar as musicas

procurar = input('Digite uma palavra para pesquisar ou enter para ver todas as musicas')

u.procurar(procurar)
#u.voltar()
#u.mostrar()
u.reproduzir('Digite o numero que quer reproduzir')

