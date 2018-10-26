class Tree:
    def __init__(self):
        self.data = [15, 30, 45, 16, 50, 20, 3]

    def subir(self, indice):
        if(self.data[indice] == None):
            return
        indice_pai = round((indice-1)/2)
        if(self.data[indice_pai] > self.data[indice]):
            self.data[indice_pai], self.data[indice] = self.data[indice], self.data[indice_pai]
            self.subir(indice_pai)


    def descer(self, pai):
        indice_pai = self.data.index(pai)
        if(self.data[indice_pai] == None):
            return False
        indice_filho_d = 2*indice_pai+2
        indice_filho_e = 2*indice_pai+1
        if indice_filho_d < len(self.data):
            if self.data[indice_filho_d] < self.data[indice_filho_e]:
                if(self.data[indice_filho_d] < self.data[indice_pai]):
                    self.data[indice_filho_d], self.data[indice_pai] = self.data[indice_pai], self.data[indice_filho_d]
                    self.descer(self.data[indice_filho_d])
            else:
                if(self.data[indice_filho_e] < self.data[indice_pai]):
                    self.data[indice_filho_e], self.data[indice_pai] = self.data[indice_pai], self.data[indice_filho_e]
                    self.descer(self.data[indice_filho_e])
        else:
            return False
            
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


def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n//2)):
        _siftup(x, i)

def _siftdown(heap, startpos, pos):
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

def _siftup(heap, pos):
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
    _siftdown(heap, startpos, pos)
       

t = [15, 30, 45, 16, 50, 20, 3]
print(t)
heapify(t)
print(t)
