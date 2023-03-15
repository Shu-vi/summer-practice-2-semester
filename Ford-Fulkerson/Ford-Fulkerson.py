
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

    # Находим случайный маршрут от истока к стоку и возвращаем список номеров вершин графа в той последовательности, в которой они идут в маршруте
    def __find_route(self) -> list:
        pass

    # Находим минимальный поток в маршруте (в списке вершин)
    def __find_min_flow(self, route):
        pass

    # Вычитаем из маршрута минимальный поток маршрута
    def __subtruct_min_from_route(self):
        pass

    # Проверяем, есть ли ещё свободные маршруты из истока в сток
    def __is_has_routes(self) -> bool:
        pass

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

g = Graph(transition_table)

print(g.get_max_total_flow())