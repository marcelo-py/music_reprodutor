import os
import playsound
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

    def reproduzir(self, numero=''):
        if numero.isnumeric():
            numero = int(numero)

            if numero <= len(self.musicas_achadas):
                playsound.playsound(self.musicas.diretorio+'/'+self.musicas_achadas[numero])
            else:
                print('nada digitado!')

#main test
a = MusicPlayer()
u = Usuario(a)
a.buscar_no_diretorio(r'C:\Users\edilm\Documents\MEGAsync Downloads\backup\Whatlisten') #esse metodo recebe o diretorio onde o usuario quer pegar as musicas
#u.mostrar()
procurar = input('Digite uma palavra para pesquisar')
u.procurar(procurar)
reproduzir = input('Digite o numero que quer reproduzir')
u.reproduzir(reproduzir)
