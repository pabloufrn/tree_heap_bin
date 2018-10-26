import heapq
class Tree:
    def __init__(self):
        self.data = [20, 10, 5, 8, 3, 30, 60]

    def subir(self, indice):
        if(self.data[indice] == None):
            return
        indice_pai = round((indice-1)/2)
        if(self.data[indice_pai] > self.data[indice]):
            self.data[indice_pai], self.data[indice] = self.data[indice], self.data[indice_pai]
            self.subir(indice_pai)
            
    def heapify(self):
       maxi = len(self.data)
       i = 0
       while i < maxi:
            index = i
            left = 2*i+1
            right = 2*i+2
            if left < maxi and self.data[left] > self.data[index]:
                index = left
            if right < maxi and self.data[right] > self.data[index]:
                index = right
            if index == i:
                return
            self.data[i], self.data[index] = self.data[index], self.data[i]
            i = index
             

    def pop(self, indice):
        filho_atual = indice
        while(self.data[filho_atual] != None):
            filho_atual = 2*filho_atual+1
        folha = round((filho_atual-1)/2)
        self.data[indice] = self.data[folha]
        self.data[folha] = None

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


    def _siftup(self, pos):
        heap = self.data
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        self._siftdown(startpos, pos)

    def _siftdown(self, startpos, pos):
        heap = self.data
        newitem = heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    def descer(self, indice_pai):
        if(self.data[indice_pai] == None):
            return

        indice_filho = 2 * indice_pai + 1
        # verifica se passou do vetor (pai é folha) e existe filho esquerdo
        if(indice_filho >= len(self.data)):
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
    

       

t = Tree()
print(t)
t.heapify()
print(t)
l = [20, 10, 5, 8, 3, 30, 60]
heapq.heapify(l)
print(l)