class Tree:
    def __init__(self):
        self.data = [15, 30, 45, 16]

    def subir(self, indice):
        if(self.data[indice] == None):
            return
        indice_pai = round((indice-1)/2)
        if(self.data[indice_pai] > self.data[indice]):
            self.data[indice_pai], self.data[indice] = self.data[indice], self.data[indice_pai]
            self.subir(indice_pai)


    def descer(self, indice):
        if(self.data[indice] == None):
            return
        indice_filho = 2*indice+1
        if(self.data[indice_pai] > self.data[indice]):
            self.data[indice_pai], self.data[indice] = self.data[indice], self.data[indice_pai]
            self.descer(indice_filho)


    def heapify(self):
        filho_atual = indice
        while(self.data[filho_atual] != None):
            filho_atual = 2*filho_atual+2
        folha = round((filho_atual-1)/2)
        indice_pai = round((folha-1)/2)

        self.descer(indice_pai)

    def pop(self, indice):
        filho_atual = indice
        while(self.data[filho_atual] != None):
            filho_atual = 2*filho_atual+1
        folha = round((filho_atual-1)/2)
        self.data[indice] = self.data[folha]
        self.data[folha] = None






    def __str__(self):
        return str(self.data)
       

t = Tree()
t.subir(3)
print(t)
