import random

"""
    -Корень и конечные узлы(листья) всегда чёрные
    -У красного узла родительский узел - чёрный
    -Все простые пути из любого узла до листьев содержут одинаковое количество чёрных узлов
    -Чёрный узел может иметь черного родителя(а может и красного)
    -Оба потомка красного узла - чёрные

    БАЛАНСИРОВКА
    1) Каждый узел либо красный, либо чёрный. Nil листья всегда чёрные.
    2) Корень дерева всегда чёрный
    3) Оба потомка красного узла всегда чёрные
    4) Путь вниз от любого листа до любого листа-потока содержит одинаковое количество чёрных узлов

    При вставке нового элемента он автоматически красный

    Алгоритм вставки. Если дерево пустое, то просто создаём корень. По умолчанию корень будет красный, его нужно сбалансировать потом
    Если дерево не пустое
        Находим место, в которое нужно добавить элемент
        Добавляем элемент
        Балансируем, после добавления
"""
class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.root.color = 'black'
            return
        node = self.__search_place(self.root, value)
        if value <= node.value:
            node.left = new_node
            new_node.parent = node
        else:
            node.right = new_node
            new_node.parent = node
        self.__fix_violation(new_node)

    def __search_place(self, node, value):
        if node is None:
            return None
        if value <= node.value:
            if node.left is None:
                return node
            return self.__search_place(node.left, value)
        else:
            if node.right is None:
                return node
            return self.__search_place(node.right, value)

    def __fix_violation(self, node):
        while node.parent is not None and node.parent.color == 'red': #Если родитель красный и он существует
            if node.parent == node.parent.parent.left: # если отец слева от дедушки
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == 'red':#Если дядя существует и он красный
                    # Случай первый - красный дядя
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else: #Если дядя чёрный
                    #Случай 2. Папа слева от дедушки. Сын справа от папы
                    if node == node.parent.right:
                        node = node.parent
                        self.__rotate_left(node)
                    #Случай 3. Папа слева от дедушки, сын слева от папы
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.__rotate_right(node.parent.parent)
            else: #Если отец справа от дедушки
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == 'red':# Если дядя красный
                    #Случай 1. Красный дядя
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else: # Если дяди чёрный
                    #Случай 2. Отец справа от дедушки. Сын слева от отца
                    if node == node.parent.left:# Если сын слева от отца
                        node = node.parent
                        self.__rotate_right(node)
                    #Случай 3. Отец справа от дедушки. Сын справа от отца
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.__rotate_left(node.parent.parent)
        self.root.color = 'black'

    def __rotate_right(self, node):
        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left


    def __rotate_left(self, node):
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    #0 - лево, 1 - право
    def print_tree(self):
        nodes = [(self.root, [])]
        while nodes:
            current_node, path = nodes.pop()
            print('Значение узла: ', current_node.value, '; цвет узла: ', current_node.color, '; двоичная последовательность: ', path)
            if current_node.left:
                nodes.append((current_node.left, path + [0]))
            if current_node.right:
                nodes.append((current_node.right, path + [1]))
    
            





rbd = RedBlackTree()
n = int(input('Введите количество чисел, которые необходимо вставить в дерево '))
for i in range(n):
    j = random.randrange(0, 50)
    rbd.insert(j)
    print('Вставили число ', j)

rbd.print_tree()