
class Node:
    def __init__(self, value):
        self.value = value
        self.rigth = None
        self.left = None
        self.down = None

    def __str__(self) -> str:
        print(self.value)

class LinkedMatrix:
    def __init__(self, filas, columnas):
        node = Node(None)
        self.root = node
    
        for j in range(columnas-1):
            node.rigth = Node(None)
            node.rigth.left = node
            node = node.rigth
        
        current = self.root
        for i in range(filas-1):
            node = Node(None)
            node_up = current
            current.down = node
            node.up = node_up
            current = node
            for j in range(columnas-1):
                node.rigth = Node(None)
                node.rigth.left = node
                node.rigth.up = node_up.rigth
                node_up.rigth.down = node.rigth
                node = node.rigth
    
    def add_player(self, fila, columna, valor):
        node = self.root
        for i in range(fila):
            node = node.down
        for j in range(columna):
            node = node.rigth
        node.value = valor

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
        self.value = "🤖"

    def depredador_position(self, i, j):
        self.linked_matrix.add_player(i, j, self.value)

    def depredador_movents(self, movent):
        pass
    def depredador_attack(self, movent):
        pass

class GameController:
    pass






# lm = LinkedMatrix(2, 2)

# lm.add_player(0, 0, 1)
# lm.add_player(0, 1, 3)
# lm.add_player(1, 0, 5)
# lm.add_player(1, 1, "👽")
# lm.mostrar()


