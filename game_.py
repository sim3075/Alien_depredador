import random
class Node:
    def __init__(self, value):
        self.value = value
        self.rigth = None
        self.left = None
        self.down = None
        self.up = None

    def __str__(self) -> str:
        print(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        current = self.head
        if(current is None):
            return
        else:
            for i in range(random.randint(1,3)):
                random_value = current.value
                current = current.rigth
            return random_value

    def add_at_tail(self, value):
        if(self.head is None):
            self.head = Node(value)
        else:
            current = self.head
            while(current.rigth is not None):
                current = current.rigth
            current.rigth = Node(value)

class LinkedMatrix:
    def __init__(self, size):
        self.size = size
        node = Node("+")
        self.root = node
        self.ll = LinkedList()

        
        self.ll.add_at_tail("+")
        self.ll.add_at_tail("-")
        self.ll.add_at_tail(" ")
        random = self.ll.traverse()
        random2 = self.ll.traverse()
        random3 = self.ll.traverse()
    
        for j in range(self.size-1):
            node.rigth = Node(random)
            node.rigth.left = node
            node = node.rigth
        
        current = self.root
        for i in range(self.size-1):
            node = Node(random2)
            node_up = current
            current.down = node
            node.up = node_up
            current = node
            for j in range(self.size-1):
                node.rigth = Node(random3)
                node.rigth.left = node
                node.rigth.up = node_up.rigth
                node_up.rigth.down = node.rigth
                node = node.rigth
    
    def add_player(self, fila, columna, valor):
        node = self.root
        for i in range(fila):
            if node is not None:
                node = node.down
        for j in range(columna):
            if node is not None:
                node = node.rigth
        node.value = valor
        return node

    def mostrar(self):
        nodo_fila = self.root
        while nodo_fila is not None:
            nodo_columna = nodo_fila
            while nodo_columna is not None:
                print(nodo_columna.value, end='\t')
                nodo_columna = nodo_columna.rigth
            print()
            nodo_fila = nodo_fila.down

class Alien:

    def __init__(self, linked_matrix):
        self.health = 50
        self.value = "👽"
        self.linked_matrix = linked_matrix

    def alien_position(self, i, j):
        self.linked_matrix.add_player(i, j, self.value)
    
    def alien_movents(self, movent):
        pass
    def alien_attack(self, movent):
        pass

class Depredador:
    def __init__(self, linked_matrix):
        self.health = 50
        self.avatar = None 
        self.linked_matrix = linked_matrix
        self.random_row = random.randint(0,self.linked_matrix.size-1)
        self.random_column = random.randint(0,self.linked_matrix.size-1)
        self.W = None
        self.A = None
        self.S = None
        self.D = None

    def depredador_position(self):
        self.avatar = self.linked_matrix.add_player(self.random_row, self.random_column, "🤖")
        self.W = self.avatar.up
        self.A = self.avatar.left
        self.S = self.avatar.down
        self.D = self.avatar.rigth

    def depredador_movents(self, movent):
        pass
    def depredador_attack(self, movent):
        pass

class GameController:
    pass






lm = LinkedMatrix(3)
depre = Depredador(lm)
depre.depredador_position()
# lm.add_player(0, 0, 1)
# lm.add_player(0, 1, 3)
# lm.add_player(1, 0, 5)
lm.add_player(1, 1, "👽")
lm.mostrar()




