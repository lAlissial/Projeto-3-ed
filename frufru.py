c = ('\033[m',         # 0 - bg sem cores
     '\033[1;41m',     # 1 - bg vermelho
     '\033[1;42m',     # 2 - bg verde
     '\033[1;43m',     # 3 - bg amarelo
     '\033[1;44m',     # 4 - bg azul
     '\033[1;45m',     # 5 - bg roxo
     '\033[1;46m',     # 6 - bg ciano
     '\033[1;47m',     # 7 - bg cinza
     '\033[7m' ,       # 8 - bg branco
     '\033[1;103m',    # 9 - bg amarelo claro
     '\033[1;97;104m', # 10 - bg azul claro
     '\033[1;102m',    # 11 - bg verde claro
     '\033[1;40m',     # 12 - bg preto
     '\033[1;100m',    # 13 - bg cinza escuro
     '\033[1;101m',    # 14 - bg vermelho claro
     '\033[1;97;105m', # 15 - bg magenta claro
     '\033[1;97;106m', # 16 - bg cyan claro
     '\033[1;31m',     # 17 - vermelho
     '\033[1;32m',     # 18 - verde
     '\033[1;33m',     # 19 - amarelo
     '\033[1;34m',     # 20 - azul
     '\033[1;35m',     # 21 - magenta
     '\033[1;36m',     # 22 - cyan
     '\033[1;37m',     # 23 - cinza claro
     '\033[1;97m',     # 24 - branco
     '\033[1;93m',     # 25 - amarelo claro
     '\033[1;94m',     # 26 - azul claro
     '\033[1;92m',     # 27 - verde claro
     '\033[1;40m',     # 28 - preto
     '\033[1;90m',     # 29 - cinza escuro
     '\033[1;91m',     # 30 - vermelho claro
     '\033[1;95m',     # 31 - magenta claro
     '\033[1;96m',     # 32 - cyan claro
     '\033[1;30m')     # 33 - preto

def leia_Int(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print(f'{c[17]}ERRO: por favor, digite um número válido.{c[0]}')
      return 0
    else:
      return n

def linha(tam=50):
  return '-' * tam


def cabecalho(txt):
  print(linha())
  print(txt.center(50))
  print(linha())


def menu(lista, texto):
    cabecalho(texto)
    cont = 1
    for item in lista:
        print(f'{c[25]}{cont}{c[0]} - {c[20]}{item}{c[0]}')
        cont += 1
    print(linha())
    opc = leia_Int('Opcão: ')
    return opc
