from frufru import *
from catalogo import *


arvore = Catalogo()


arvore.inserir(1, 'a', 2018, 'Um album legal')
arvore.inserir(7, 'f', 2019, 'Um album')
arvore.inserir(3, 'z', 2019, 'Um albumzito')
arvore.inserir(6, 'e', 2021, 'Um albumzits')
arvore.inserir(4, 'b', 2004, 'Um album aí')
arvore.inserir(2, 'h', 2019, 'Um album fran')
arvore.inserir(5, 'n ', 2019, 'Um album japs')
arvore.inserir(12, 'p ', 2017, 'Um album da galera')
arvore.inserir(21, 's', 2021, 'Um album do desespero')
arvore.inserir(34, 'v', 2009, 'do teste')
arvore.inserir(75, 'w', 2002, 'do teste')
arvore.inserir(90, 'l', 2001, 'do teste')
arvore.inserir(120, 'j', 2018, 'do teste')
arvore.inserir(200, 'y', 2018, 'do teste')
arvore.inserir(1, 'c', 2018, 'do teste')



# arvore.insert(1, 'Hey', 2018, 'Um album legal')
# arvore.insert(7, 'Hello', 2019, 'Um album')
# arvore.insert(3, 'Hallo', 2019, 'Um albumzito')
# arvore.insert(6, 'Привет', 2021, 'Um albumzits')
# arvore.insert(4, 'Olá', 2019, 'Um album aí')
# arvore.insert(2, 'Bonjour', 2019, 'Um album fran')
# arvore.insert(5, 'こんにちは ', 2019, 'Um album japs')
# arvore.insert(12, 'Aloalo ', 2017, 'Um album da galera')
# arvore.insert(21, 'Socorro', 2021, 'Um album do desespero')
# arvore.insert(34, 'Testando1', 2018, 'do teste')
# arvore.insert(75, 'Testando2', 2018, 'do teste')
# arvore.insert(90, 'Testando3', 2018, 'do teste')
# arvore.insert(120, 'Testando4', 2018, 'do teste')
# arvore.insert(200, 'Testando5', 2018, 'do teste')
#arvore.insert(1, 'Testando', 2018, 'do teste')

print(arvore)
print('Altura:', arvore._profundidade)
print('Nome do nó que tem id 1:',arvore.buscarId(1, arvore.raiz).nome)

listaParaOrdemAlfabetica = []
print(arvore.ordemAlfabetica(listaParaOrdemAlfabetica, arvore.raiz))
print()
listaparabuscarano = []
lista2parabuscarano = []
guardandolista = arvore.buscarAnos(listaparabuscarano, arvore.raiz, 2018, lista2parabuscarano)

for i in listaparabuscarano:
  print(f'Nome:{i.nome}\nAno:{i.ano}\nAlbum:{i.album}')
# print(f'*' * 50)
# print(f"{c[10]}{'CATÁLOGO DE MÚSICAS':^50}{c[0]}")
# print(f'*' * 50)

# while True:
#     resp = menu(["Incluir registro de uma música", "Buscar uma música pelo ID", "Buscar músicas pelo ano", "Listagem de todas as músicas do catálogo, por ordem alfabética, crescente", "Exibir a altura da árvore", "Sair do Sistema"],"MENU PRINCIPAL")
#     if resp == 1:CHECK
#         pass
#     if resp == 2:CHECK
#         pass
#     if resp == 3:CHECK
#         pass
#     if resp == 4:
#         pass
#     if resp == 5:
#         pass
#     if resp == 6:CHECK
#         pass
#     if resp == 7: CHECK
#         pass