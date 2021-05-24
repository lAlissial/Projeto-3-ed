from frufru import *
from catalogo import *


arvore = Catalogo()

# arvore.inserir(50, 'a', 2018, 'Um album legal')
# arvore.inserir(12, 'f', 2019, 'Um album')
# arvore.inserir(9, 'z', 2019, 'Um albumzito')
# arvore.inserir(21, 'e', 2021, 'Um albumzits')
# arvore.inserir(87, 'b', 2004, 'Um album aí')
# arvore.inserir(33, 'h', 2019, 'Um album please')
# arvore.inserir(5, 'n ', 2019, 'Um album help')
# arvore.inserir(6, 'p ', 2017, 'Um album da galera')
# arvore.inserir(2, 's', 2021, 'Um album do desespero')
# arvore.inserir(34, 'v', 2009, 'Album do teste')
# arvore.inserir(75, 'w', 2002, 'Album teste')
# arvore.inserir(2, 'l', 2001, 'Album teste')
# arvore.inserir(120, 'j', 2015, 'Album teste')
# arvore.inserir(59, 'y', 2011, 'Album teste')
# arvore.inserir(80, 'y', 2006, 'Album teste')
#arvore.inserir(1, 'c', 2018, 'do teste')


print(f'*' * 50)
print(f"{c[10]}{'APLICATIVO DE STREAM':^50}{c[0]}")
print(f'*' * 50)

while True:
    resp = menu(["Incluir registro de uma música", "Buscar uma música pelo ID", "Buscar músicas pelo ano", "Listagem das músicas por ordem alfabética", "Altura da árvore", "Exibir árvore", "Sair do Sistema"],"CATÁLOGO DE MÚSICAS")
    if resp == 1:
        idz = int(input('Id: '))
        nomez = str(input('Nome da música: '))
        anoz = int(input('Ano: '))
        albumz = str(input('Nome do Album: '))
        arvore.inserir(idz, nomez, anoz, albumz)
    if resp == 2:
        idqualquer = int(input('Informe o id que deseja buscar: '))
        buscando = arvore.buscarId(idqualquer, arvore.raiz)
        if buscando:
            print(f'{c[27]}Id encontrado!{c[0]}')
            print(f'Nome: {buscando.nome}\nAno: {buscando.ano}\nAlbum: {buscando.album}\nId: {buscando.id}')
        else:
            print(f'{c[30]}Id não existe no catálogo!{c[0]}')
    if resp == 3:
        n = int(input('Ano: '))
        lista1parabuscarano = []
        lista2parabuscarano = []
        guardandoresp = arvore.buscarAnos(lista1parabuscarano, arvore.raiz, n, lista2parabuscarano)
        if len(guardandoresp) > 0:
            print()
            for i in guardandoresp:
                print(f'Nome: {i.nome}\nAno: {i.ano}\nAlbum: {i.album}\n')
        else:
            print(f'{c[30]}Nenhuma música encontrada{c[0]}')
    if resp == 4:
        listaParaOrdemAlfabetica = []
        print(arvore.ordemAlfabetica(listaParaOrdemAlfabetica, arvore.raiz))
    if resp == 5:
        print(f'{c[31]}Altura:{c[0]}{arvore.calcAltura(arvore.raiz)}')
    if resp == 6:
        print(f'{c[18]}EXIBIÇÃO DA ÁRVORE{c[0]}')
        print(arvore)
    if resp == 7:
        cabecalho('ATÉ A PRÓXIMA')
        break
      
