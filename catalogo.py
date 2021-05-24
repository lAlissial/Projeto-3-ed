class Catalogo:
  class Registro:


    def __init__(self, id=None, nome=None, ano=None, album=None, esquerda=None, direita=None, balanco=0, pai=None):
      self._id = id
      self._nome = nome
      self._ano = ano
      self._album = album
      self._esquerda = esquerda
      self._direita = direita
      self._balanco = balanco
      self._pai = pai

    # get
    @property
    def id(self):
      return self._id

    # set
    @id.setter
    def id(self, novo):
      self._id = novo

    # get
    @property
    def nome(self):
      return self._nome

    # set
    @nome.setter
    def nome(self, novo):
      self._nome = novo

    # get
    @property
    def ano(self):
      return self._ano

    # set
    @ano.setter
    def ano(self, novo):
      self._ano = novo

    # get
    @property
    def album(self):
      return self._album

    # set
    @album.setter
    def album(self, novo):
      self._album = novo

    # get
    @property
    def esquerda(self):
      return self._esquerda

    # set
    @esquerda.setter
    def esquerda(self, novo):
        self._esquerda = novo

    # get
    @property
    def direita(self):
      return self._direita

    # set
    @direita.setter
    def direita(self, novo):
        self._direita = novo

    # get
    @property
    def pai(self):
      return self._pai

    # set
    @pai.setter
    def pai(self, novo):
        self._pai = novo

    # get
    @property
    def balanco(self):
      return self._balanco

    # set
    @balanco.setter
    def balanco(self, novo):
        self._balanco = novo

  def __init__(self):
    self._raiz = None
    self._profundidade = None
    self._caractmax = None

  # get
  @property
  def raiz(self):
    return self._raiz

  # set
  @raiz.setter
  def raiz(self, novo):
      self._raiz = novo

  #get
  @property
  def profundidade(self):
    return self._profundidade

  # set
  @profundidade.setter
  def profundidade(self, novo):
      self._profundidade = novo

  # get
  @property
  def caractmax(self):
    return self._caractmax

  # set
  @caractmax.setter
  def caractmax(self, novo):
      self._caractmax = novo

  def inserir(self, id, nome, ano, album):
    if (id == None) or (nome == None) or (ano == None) or (album == None):
      return
    if (not self.raiz):
      self.raiz = Catalogo.Registro(id=id, nome=nome, ano=ano, album=album)
      return
    else:
      self.inserirRecursivo(self.raiz, id, nome, ano, album)
      return

  def inserirRecursivo(self, no, id, nome, ano, album):
    if (id == no.id):
      return

    if id < no.id:
      if no.esquerda:
        self.inserirRecursivo(no.esquerda, id, nome, ano, album)
      else:
        no.esquerda = Catalogo.Registro(id=id, nome=nome, ano=ano, album=album, pai=no)
        self.attbalanco(no.esquerda)
    else:
      if no.direita:
        self.inserirRecursivo(no.direita, id, nome, ano, album)
      else:
        no.direita = Catalogo.Registro(id=id, nome=nome, ano=ano, album=album, pai=no)
        self.attbalanco(no.direita)
    return

  def attbalanco(self, no):
    if (no.balanco > 1 or no.balanco < -1):
      self.rebalanco(no)
      return
    if no.pai:
      if no.pai.esquerda is no:
        no.pai.balanco += 1
      elif no.pai.direita is no:
        no.pai.balanco -= 1

      if no.pai.balanco != 0:
        self.attbalanco(no.pai)

  def rotacaoEsquerda(self, no):
    novonoraiz = no.direita
    no.direita = novonoraiz.esquerda
    if (novonoraiz.esquerda):
      novonoraiz.esquerda.pai = no
    novonoraiz.pai = no.pai
    if no is self.raiz:
      self.raiz = novonoraiz
    else:
      if no.pai.esquerda is no:
        no.pai.esquerda = novonoraiz
      else:
        no.pai.direita = novonoraiz
    novonoraiz.esquerda = no
    no.pai = novonoraiz
    no.balanco = no.balanco + 1 - min(novonoraiz.balanco, 0)
    novonoraiz.balanco = novonoraiz.balanco + 1 + max(no.balanco, 0)

  def rotacaoDireita(self, no):
    novonoraiz = no.esquerda
    no.esquerda = novonoraiz.direita
    if (novonoraiz.direita):
      novonoraiz.direita.pai = no
    novonoraiz.pai = no.pai
    if no is self.raiz:
      self.raiz = novonoraiz
    else:
      if no.pai.direita is no:
        no.pai.direita = novonoraiz
      else:
        no.pai.esquerda = novonoraiz
    novonoraiz.direita = no
    no.pai = novonoraiz
    no.balanco = no.balanco - 1 - max(novonoraiz.balanco, 0)
    novonoraiz.balanco = novonoraiz.balanco - 1 + min(no.balanco, 0)

  def rebalanco(self, no):
    if no.balanco < 0:
      if no.direita.balanco > 0:
        self.rotacaoDireita(no.direita)
        self.rotacaoEsquerda(no)
      else:
        self.rotacaoEsquerda(no)
    elif no.balanco > 0:
      if no.esquerda.balanco < 0:
        self.rotacaoEsquerda(no.esquerda)
        self.rotacaoDireita(no)
      else:
        self.rotacaoDireita(no)

  def buscarId(self, data, no):
    if not no:
      return None
    elif no.id == data:
      return no
    elif data > no.id:
      return self.buscarId(data, no.direita)
    elif data < no.id:
      return self.buscarId(data, no.esquerda)

  def calcAltura(self, raizita):
    profunds_esq = 0
    profunds_dir = 0
    if raizita.esquerda:
      profunds_esq = self.calcAltura(raizita.esquerda)
    if raizita.direita:
      profunds_dir = self.calcAltura(raizita._direita)
    return 1 + max(profunds_esq, profunds_dir)

  def guardandoArvoreLista(self, lista, arvore):
    if arvore != None:
      self.guardandoArvoreLista(lista, arvore.esquerda)
      lista.append(arvore)
      self.guardandoArvoreLista(lista, arvore.direita)
    return lista

  def ordemAlfabetica(self, lista, arvore):
    array = self.guardandoArvoreLista(lista, arvore)
    ordenada = sorted(array, key=lambda registro: registro._nome)
    outputzin = ''
    for e in ordenada:
      outputzin += f'{e.nome}\n'
    return outputzin

  def buscarAnos(self, lista1, arvore, ano, lista2):
    array = self.guardandoArvoreLista(lista1, arvore)
    ordenada = sorted(array, key=lambda registro: registro._ano)
    ini = 0
    fim = len(ordenada)-1
    meio = (ini + fim) // 2

    quebrando1 = ordenada[:meio]
    ini1 = 0
    fim1 = len(quebrando1)-1
    while ini1 <= fim1:
      meio1 = (ini1 + fim1) // 2
      if ano >= quebrando1[meio1].ano:
        if ano == quebrando1[meio1].ano:
          lista2.append(quebrando1[meio1])
        ini1 = meio1 + 1
      else:
        fim1 = meio1 - 1

    quebrando2 = ordenada[meio:]
    ini2 = 0
    fim2 = len(quebrando2)-1
    while ini2 <= fim2:
      meio2 = (ini2 + fim2) // 2
      if ano >= quebrando2[meio2].ano:
        if ano == quebrando2[meio2].ano:
          lista2.append(quebrando2[meio2])
        ini2 = meio2 + 1
      else:
        fim2 = meio2 - 1

    #busca resto
    for i in ordenada:
      if i.ano == ano:
        if i not in lista2:
          lista2.append(i)

    return lista2

  def calcProfeCarac(self):
    if (not self.raiz):
      self._profundidade = 0
      self._caractmax = 1
      return
    self._profundidade = 0
    self._caractmax = 1
    l= []
    l.append((self.raiz, 1, len(str(self.raiz.id))))
    while len(l):
      no, profundidade, chars = l.pop(0)
      self._profundidade = max(self._profundidade, profundidade)
      self._caractmax = max(self._caractmax, chars)
      if no.esquerda:
        l.append((no.esquerda, profundidade + 1, len(str(no.esquerda.id))))
      if no.direita:
        l.append((no.direita, profundidade + 1, len(str(no.direita.id))))
    return
  
  def __str__(self): #percorre e printa
    self.calcProfeCarac()
    if (self._profundidade == 0):
      return ""
    s = ""
    poPrint = []
    level = 0
    poPrint.append((1, self._raiz))
    while len(poPrint):
      nolev, no = poPrint.pop(0)
      if (not no):
        if (self._profundidade - nolev + 1) <= 0:
          continue
        if (nolev != level):
          s += "\n"
          s += " " * int((self._caractmax) * (2 ** (self._profundidade - nolev) - 1))
          level = nolev
        s += " " * (self._caractmax) * (2 ** (self._profundidade - nolev + 1) - 1)
        s += " " * self._caractmax
        poPrint.append((nolev + 1, None))
        poPrint.append((nolev + 1, None))
        continue
      if (nolev != level):
        s += "\n"
        s += " " * (self._caractmax) * (2 ** (self._profundidade - nolev) - 1)
        level = nolev
      for i in range(int(self._caractmax - len(str(no.id)))):
        s += ""
      s += str(no.id)
      s += " " * (self._caractmax) * (2 ** (self._profundidade - nolev + 1) - 1)
      if no.esquerda:
        poPrint.append((nolev + 1, no.esquerda))
      else:
        poPrint.append((nolev + 1, None))
      if no.direita:
        poPrint.append((nolev + 1, no.direita))
      else:
        poPrint.append((nolev + 1, None))
    s += "\n"
    return s
