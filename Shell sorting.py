import random

#В сортировке Шелла происходит сортировка вставками, но соритруются
#конкретные подмассивы, расстоянии между элементами которых равно d,
#где d = n // 2 , при чём с каждой итерацией d уменьшается вдвое, пока не станет равен нулю


def print_array(message, arr):
    result = message
    for i in range(len(arr)):
        result += "  " + str(arr[i])
    print(result)

#На вход массив arr
#start - позиция, с которой нужно начать сдвигать элементы право на шаг step
#lastIndex - последняя позиция, которую надо сдвинуть вправо
#[start; lastIndex]
def shift_right(arr, start, last_index, step):
    i = last_index
    while i >= start:
        arr[i + step] = arr[i]
        i -= step

#arr - исходный массив, который сортируем. start - индекс первого элемента, который будем сортировать.
#finish - индекс последнего элемента(не включительно). step - шаг, с которым мы будем просматривать элементы в списке, начиная со start
#Сортирует только один конкретный подмассив
def insertion_sort(arr, start, finish, step):
    last_index = start + step
    while last_index < finish:
        cursor = last_index - step
        while (arr[cursor] > arr[last_index]) and (cursor != start):
            cursor -= step

        if (arr[cursor] > arr[last_index]) and (cursor == start):
            temp = arr[last_index]
            shift_right(arr, start, last_index - step, step)
            arr[cursor] = temp
        elif (arr[cursor] <= arr[last_index]):
            cursor += step
            temp = arr[last_index]
            shift_right(arr, cursor, last_index - step, step)
            arr[cursor] = temp
        last_index += step

n = int(input('Введите длину массива: '))
arr = [random.randrange(-20, 21) for _ in range(n)]
print_array("Массив до сортировки: ", arr)

d = n // 2
while d > 0:
    for i in range(d):
        insertion_sort(arr, i, n, d)
    d //= 2
print_array("Массив после сортировки: ", arr)






