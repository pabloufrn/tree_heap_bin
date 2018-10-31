import heapq
class Tree:
    def __init__(self):
        self.data = [20, 10, 5, 8, 3, 30, 60]

    def subir(self, indice_filho):
        if(indice_filho == 0):
            return 
        if(self.data[indice_filho] == None):
            return

        indice_pai = (indice_filho-1) // 2
        if(self.data[indice_pai] > self.data[indice_filho]):
            self.data[indice_pai], self.data[indice_filho] = self.data[indice_filho], self.data[indice_pai]
            self.subir(indice_pai)

    def descer(self, indice_pai):
        if(self.data[indice_pai] == None):
            return

        indice_filho = 2 * indice_pai + 1
        # verifica se passou do vetor (pai é folha) e existe filho esquerdo
        if(indice_filho >= len(self.data) or not self.data[indice_filho]):
            return 

        # verifica se o filho a direita existe e é menor
        if(self.data[indice_filho+1] and self.data[indice_filho+1] < self.data[indice_filho]):
            indice_filho += 1

        # verifica se não há condição de troca
        if(self.data[indice_filho] >= self.data[indice_pai]):
            return 

        # troca e chama o descer
        self.data[indice_filho], self.data[indice_pai] = self.data[indice_pai], self.data[indice_filho]
        self.descer(indice_filho)

    def push(self, valor):
        n = len(self.data)
        folha = len(n-1)
        while folha > 0 and self.data[folha] == None:
            folha -= 1

        self.data.append()
        if(folha == n-1):
            """ Adiciona mais elementos da lista ( dobro do último nível)"""
            self.data += ( n + 1 ) * [None] 

        self.data[folha] = valor
        subir(folha)

             
    def pop(self):
        folha = len(self.data-1)
        while folha > 0 and self.data[folha] == None:
            folha -= 1
        self.data[0] = self.data[folha]
        self.data[folha] = None

        if(folha == n // 2):
            # tira o ultimo nivel
            self.data = self.data[:n//2]

        self.descer(0)

    def __str__(self):
        return str(self.data)

    def heapify(self):
        n = len(self.data)
        """
        Se calcularmos pai do último indice temos que: 
        indice_pai = (indice-1) // 2
        indice_pai = (n-2) // 2
        Se n é par, a divisão é perfeita, então:
            indice_pai = ( n - 2 ) / 2
            indice_pai = 2 * ( n / 2 - 1 ) / 2
            indice_pai =  n / 2 - 1

        Se n é ímpar, podemos considerar o cálculo do pai 
        a partir do último filho à esquerda da lista, que 
        fica na posição n-2, assim:
            indice_pai = ( n - 3 ) / 2
            indice_pai = ( n - 2 - 1 ) / 2
            indice_pai = 2 * ( n/2 - 1 - 1 / 2 ) / 2
            indice_pai = n/2 - 1/2 -1
            indice_pai = n - 1 / 2 - 1
        Se usamos a função piso, veremos que, para n impar:
            n - 1 / 2 = n // 2
        E para n par:
            n / 2 =  n // 2 
        Assim concluimos que o indice do nó mais a direita e mais profundo que não é folha é:
            indice_pai = n // 2 - 1

        Percorreremos então o intervalo [0, n // 2) da direita para a esquerda chamando a função descer.
        """
        for i in reversed(range(n//2)):
            self.descer(i)
    

       

t = Tree()
print(t)
t.heapify()
print(t)
l = [20, 10, 5, 8, 3, 30, 60]
heapq.heapify(l)
print(l)
print("mudei um negócio aqui")
