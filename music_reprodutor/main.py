'''BY:0M      O00111
   000  A1   L1  000
   100    RCE    000
   110           001   
   '''


from music_reprodutor import *
a = MusicPlayer()
u = Usuario(a)
a.buscar_no_diretorio(r'C:\Users\NOME DOUSUARIO\Downloads\...') #esse metodo recebe o diretorio onde o usuario quer pegar as musicas

while True:
    print('>opções<'.center(28, '-'))
    opcao = int(input('''   0 => Mostrar musicas
     1 => Procurar música
     2 => reproduzir modo dado/aleatório
     3 => Voltar'''))

    if opcao == 0:
        u.mostrar()

    elif opcao == 1:
        palavra = input('Digite a palavra chave da pesquisa ou der enter para mostrar todas as musicas')
        u.procurar(palavra)

    if opcao == 2:
        u.reproduzir('Digite o numero que quer reproduzir')

    elif opcao == 3:
        u.voltar()

    else:
        print('Opção invalida! ')
