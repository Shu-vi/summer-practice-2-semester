
"""
    Пусть граф задаётся двумерным массивом
    {
    {Состояние_из_которого_переходят1, состояние_в_которое_переходят1, мощность потока1}
    {Состояние_из_которого_переходят2, состояние_в_которое_переходят2, мощность потока2}
    {Состояние_из_которого_переходят3, состояние_в_которое_переходят3, мощность потока3}
    {Состояние_из_которого_переходят4, состояние_в_которое_переходят4, мощность потока4}
    }
    и номерами двух вершин - истока и стока
"""

class Graph:
    def __init__(self, transition_table, source_node, stock_node):
        self.__transition_table = transition_table
        self.__source_node = source_node
        self.__stock_node = stock_node

    #СДЕЛАНО
    # Возвращаем мощность потока между вершинами по номерам вершин
    def __get_flow_between_nodes(self, node_1=0, node_2=0) -> int:
        for i in self.__transition_table:
            if (i[0] == node_1) and (i[1] == node_2):
                return i[2]

    # Находим случайный маршрут от истока к стоку и возвращаем список номеров вершин графа в той последовательности, в которой они идут в маршруте
    def __find_route(self) -> list:
        route = []
        visited = set()
        queue = [(self.__source_node, [self.__source_node])]
        while queue:
            (vertex, path) = queue.pop(0)
            if vertex == self.__stock_node:
                route = path
                break
            if vertex not in visited:
                visited.add(vertex)
                for transition in self.__transition_table:
                    if transition[0] == vertex:
                        queue.append((transition[1], path + [transition[1]]))
        return route

    #СДЕЛАНО
    # Находим минимальный поток в маршруте (в списке вершин)
    def __find_min_flow(self, route):
        min_flow = self.__get_flow_between_nodes(route[0], route[1])
        for i in range(len(route) - 1):
            flow = self.__get_flow_between_nodes(route[i], route[i+1])
            if flow < min_flow:
                min_flow = flow
        return min_flow

    #СДЕЛАНО
    # Вычитаем из маршрута минимальный поток маршрута
    def __subtruct_min_from_route(self, route, min_flow):
        for i in range(len(route) - 1):
            for j in self.__transition_table:
                if j[0] == route[i] and j[1] == route[i+1]:
                    j[2] -= min_flow

    #СДЕЛАНО
    # Вычисляет, можно ли двигаться из node_1 в node_2
    def __is_can_move(self, node_1, node_2) -> bool:
        return self.__get_flow_between_nodes(node_1, node_2) > 0

    #СДЕЛАНО
    # Проверяем, есть ли ещё свободные маршруты из истока в сток
    def __is_has_routes(self) -> bool:
        visited = set()
        stack = []
        visited.add(self.__source_node)
        stack.append(self.__source_node)
        is_found_route = False
        while stack:
            is_found_node = False
            for i in self.__transition_table:
                if (i[0] == stack[len(stack) - 1]) and (not i[1] in visited) and self.__is_can_move(i[0], i[1]):
                    visited.add(i[1])
                    stack.append(i[1])
                    is_found_node = True
                    if i[1] == self.__source_node:
                        return True
            if not is_found_node:
                stack.pop()
        return is_found_route

    #СДЕЛАНО
    def get_max_total_flow(self) -> int:
        max_total_flow = 0
        while self.__is_has_routes():
            route = self.__find_route()
            min_flow = self.__find_min_flow(route)
            self.__subtruct_min_from_route(route, min_flow)
            max_total_flow += min_flow
        return max_total_flow
    
transition_table = [
    [0, 1, 10],
    [1, 2, 5],
    [2, 6, 8],
    [1, 3, 7],
    [3, 2, 6],
    [0, 3, 2],
    [3, 6, 2],
    [0, 4, 4],
    [4, 5, 10],
    [5, 6, 13]
]

g = Graph(transition_table, 0, 6)

#print(g.__get_flow_between_nodes())