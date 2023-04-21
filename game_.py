import random
class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.down = None
        self.up = None

    def __str__(self) -> str:
        return self.value

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
                current = current.right
            return random_value

    def add_at_tail(self, value):
        if(self.head is None):
            self.head = Node(value)
        else:
            current = self.head
            while(current.right is not None):
                current = current.right
            current.right = Node(value)

class LinkedMatrix:
    
    def __init__(self, size):
        self.ll = LinkedList()
        self.ll.add_at_tail("+")
        self.ll.add_at_tail("-")
        self.ll.add_at_tail(" ")
        random1 = self.ll.traverse()
        random2 = self.ll.traverse()
        random3 = self.ll.traverse()
        self.size = size
        node = Node(random)
        self.root = node

        
        for j in range(self.size-1):
            node.right = Node(random1)
            node.right.left = node
            node = node.right
        
        current = self.root
        for i in range(self.size-1):
            node = Node(random2)
            node_up = current
            current.down = node
            node.up = node_up
            current = node
            for j in range(self.size-1):
                node.right = Node(random3)
                node.right.left = node
                node.right.up = node_up.right
                node_up.right.down = node.right
                node = node.right
    
    def add_player(self, fila, columna, valor):
        node = self.root
        for i in range(fila):
            if node is not None:
                node = node.down
        for j in range(columna):
            if node is not None:
                node = node.right
        node.value = valor
        return node

    def mostrar(self):
        nodo_fila = self.root
        while nodo_fila is not None:
            nodo_columna = nodo_fila
            while nodo_columna is not None:
                print(nodo_columna.value, end='\t')
                nodo_columna = nodo_columna.right
            print()
            nodo_fila = nodo_fila.down

class Alien:

    def __init__(self, linked_matrix, i, j):
        self.health = 50
        self.value = "👽"
        self.i = i
        self.j = j
        self.linked_matrix = linked_matrix
        self.avatar = self.linked_matrix.add_player(i, j, "👽")

    # def alien_position(self, i, j):
    #     self.linked_matrix.add_player(i, j, self.value)
    
    def alien_movents(self, movent):
        current_node = self.avatar
        if movent == "W"  and self.avatar.up.value is not None:
            prox_node = self.avatar.up

        elif movent == "A" and self.avatar.left.value is not None:
            prox_node = self.avatar.left

        elif movent == "S" and self.avatar.down.value is not None:
            prox_node = self.avatar.down
        
        elif movent == "D" and self.avatar.right.value is not None:
            prox_node = self.avatar.right

        if prox_node.value == "+":
            self.health += 10
            self.avatar = prox_node
            current_node.value = " "
            prox_node.value = "👽"
        elif prox_node.value == "-":
            self.health -= 10
            self.avatar = prox_node
            current_node.value = " "
            prox_node.value = "👽"
        elif prox_node.value == " ":
            self.health += 0
            self.avatar = prox_node
            current_node.value = " "
            prox_node.value = "👽"
        elif prox_node.value == "🤖":
            self.health -= 25

        elif prox_node.value is None:
            self.avatar = self.avatar

    def alien_attack(self):
        if self.avatar.right is not None:
            if (self.avatar.right.value == "🤖" ):
                return True
        if self.avatar.left is not None:
            if self.avatar.left.value == "🤖":
                return True
        if not (self.avatar.up is None):
            if self.avatar.up.value == "🤖":
                return True
        if not (self.avatar.down is None):
            if self.avatar.down.value == "🤖":
                return True
        else:
            return False

class Depredador:

    def __init__(self, linked_matrix):
        self.ll = LinkedList()
        self.ll.add_at_tail("W")
        self.ll.add_at_tail("A")
        self.ll.add_at_tail("S")
        self.ll.add_at_tail("D")
        self.health = 50
        self.linked_matrix = linked_matrix
        self.random_row = random.randint(0,self.linked_matrix.size-1)
        self.random_column = random.randint(0,self.linked_matrix.size-1)
        self.avatar = self.linked_matrix.add_player(self.random_row, self.random_column, "🤖")

    def depredador_movents(self):
        while(True):
            try:
                random_move = self.ll.traverse()
                current_node = self.avatar
                if random_move == "W":
                    prox_node = self.avatar.up

                elif random_move == "A":
                    prox_node = self.avatar.left

                elif random_move == "S":
                    prox_node = self.avatar.down
                
                elif random_move == "D":
                    prox_node = self.avatar.right
                    
                if prox_node.value == "+":
                    self.health += 10
                    self.avatar = prox_node
                    current_node.value = " "
                    prox_node.value = "🤖"
                elif prox_node.value == "-":
                    self.health -= 10
                    self.avatar = prox_node
                    current_node.value = " "
                    prox_node.value = "🤖"
                elif prox_node.value == " ":
                    self.health += 0
                    self.avatar = prox_node
                    current_node.value = " "
                    prox_node.value = "🤖"
                elif prox_node.value is None:
                    self.avatar = self.avatar
                break
            except:
                pass

class GameController:
    def __init__(self, size):
      self.linked_matrix = LinkedMatrix(size)
      self.alien = None
      self.depredador = Depredador(self.linked_matrix)

    def start(self):
        i = int(input("Fila en la que quieres colocar al Alien: "))
        j = int(input("Columna en la que quieres colocar al Alien: "))
        self.alien = Alien(self.linked_matrix,i, j)
        self.depredador.depredador_movents()

        turno = 0
        while self.alien.health > 0 and self.depredador.health > 0:
            print(f"Vida del Depredador: {self.depredador.health}")
            print(f"Vida del Alien: {self.alien.health}")
            print(f"Turno {turno}:")

            if turno % 2 == 0:
                # Turno del Alien
                accion = input("Puedes moverte o atacar (M/A): ")
                if accion == "M":
                    direccion = input("¿En qué dirección quieres moverte? (W/S/A/D): ")
                    self.alien.alien_movents(direccion)
                elif accion == "A":
                    if self.alien.alien_attack():
                        self.depredador.health -= 10
            else:
                # Turno del Depredador
                self.depredador.depredador_movents()
            print()
            self.linked_matrix.mostrar()
            print()
            turno += 1
        if self.alien.health <= 0:
            print("El Depredador ganó!")
        else:
            print("El Alien ganó!")




tam = int(input("Ingrese el tamaño de la matriz: "))
game = GameController(tam)
game.start()





