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
        self.NIL = Node(99999)
        self.NIL.color = 'black'
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        if self.root == self.NIL:
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
        self.__fix_insert(new_node)

    def __search_place(self, node, value):
        if value <= node.value:
            if node.left == self.NIL:
                return node
            return self.__search_place(node.left, value)
        else:
            if node.right == self.NIL:
                return node
            return self.__search_place(node.right, value)


    def __search_node(self, value):
        node = self.root
        while node != self.NIL:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right

    def __fix_insert(self, node):
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
        if left.right != self.NIL:
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
        if right.left != self.NIL:
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
        if self.root == self.NIL:
            print('Дерево пусто')
            return
        nodes = [(self.root, [])]
        while nodes:
            current_node, path = nodes.pop()
            print('Значение узла: ', current_node.value, '; цвет узла: ', current_node.color, '; двоичная последовательность: ', path)
            if current_node.left != self.NIL:
                nodes.append((current_node.left, path + [0]))
            if current_node.right != self.NIL:
                nodes.append((current_node.right, path + [1]))

    def __delete_fix(self, node):
            while node != self.root and node.color == 'black':
                if node == node.parent.left:
                    nodes_brother = node.parent.right
                    # 1 случай брат красный
                    if nodes_brother.color == 'red':
                        nodes_brother.color = 'black'
                        node.parent.color = 'red'
                        self.__rotate_left(node.parent)
                        nodes_brother = node.parent.right
                    # 2 случай оба ребёнка брата чёрные
                    if nodes_brother.left.color == 'black' and nodes_brother.right.color == 'black':
                        nodes_brother.color = 'red' 
                        node = node.parent
                    else:
                        # 3 случай правый ребенок брата чёрный
                        if nodes_brother.right.color == 'black':
                            nodes_brother.left.color = 'black'
                            nodes_brother.color = 'red'
                            self.__rotate_right(nodes_brother)
                            nodes_brother = node.parent.right
                        # 4 случай правый ребенок брата красный
                        nodes_brother.color = node.parent.color 
                        node.parent.color = 'black' 
                        nodes_brother.right.color = 'black' 
                        self.__rotate_left(node.parent)
                        node = self.root
                else:
                    nodes_brother = node.parent.left
                    # 1 случай брат красный
                    if nodes_brother.color == 'red':
                        nodes_brother.color = 'black'
                        node.parent.color = 'red'
                        self.__rotate_right(node.parent)
                        nodes_brother = node.parent.left
                    # 2 случай оба ребёнка брата чёрные
                    if nodes_brother.right.color == 'black' and nodes_brother.left.color == 'black':
                        nodes_brother.color = 'red' 
                        node = node.parent 
                    else:
                        # 3 случай случай правый ребенок брата чёрный
                        if nodes_brother.left.color == 'black':
                            nodes_brother.right.color = 'black'
                            nodes_brother.color = 'red'
                            self.__rotate_left(nodes_brother)
                            nodes_brother = node.parent.left
                        # 4 случай правый ребенок брата красный
                        nodes_brother.color = node.parent.color 
                        node.parent.color = 'black' 
                        nodes_brother.left.color = 'black' 
                        self.__rotate_right(node.parent)
                        node = self.root
            node.color = 'black'

    def delete(self, value):
        node = self.__search_node(value)
        if node == self.NIL:
            return

        temp = node
        temp_orig_color = temp.color 
        
        # 1 случай
        if node.left == self.NIL:
            temp_2 = node.right 
            self.__transplant(node, node.right)
        # 2 случай
        elif node.right == self.NIL:
            temp_2 = node.left
            self.__transplant(node, node.left)
        # 3 случай
        else:
            temp = self.__minimum(node.right)
            temp_orig_color = temp.color
            temp_2 = temp.right 
            
            if temp.parent == node:
                temp_2.parent = temp
            else:
                self.__transplant(temp, temp.right)
                temp.right = node.right
                temp.right.parent = temp
            
            self.__transplant(node, temp)
            temp.left = node.left 
            temp.left.parent = temp 
            temp.color = node.color
        if temp_orig_color == 'black':
            self.__delete_fix(temp_2)

    #Функция забывает о корне node_1, вешая на его место корень node_2
    def __transplant(self, node_1, node_2):
        if node_1.parent == None:
            self.root = node_2
        elif node_1 == node_1.parent.left:
            node_1.parent.left = node_2 
        else:
            node_1.parent.right = node_2
        node_2.parent = node_1.parent

    def __minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node


rbt = RedBlackTree()


n = int(input('Введите количество чисел, которые необходимо вставить в дерево '))

for i in range(n):
    rbt.insert(random.randrange(0, 50))

rbt.print_tree()

inp = ''
while True:
    inp = str(input('Введите номер числа, которое хотите удалить из дерева. Для выхода введите "Выход" '))
    if inp!= 'Выход':
        inp = int(inp)
    else:
        exit(0)
    rbt.delete(inp)
    rbt.print_tree()