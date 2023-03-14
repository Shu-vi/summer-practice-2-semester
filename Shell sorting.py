import random

n = int(input('Введите длину массива '))
arr = []
i = 0

while i < n:
    arr.append(random.randrange(-20, 21))
    i += 1

print('Массив до сортировки ', arr)

#В сортировке Шелла происходит сортировка вставками, но соритруются
#конкретные подмассивы, расстоянии между элементами которых равно d,
#где d = n // 2 , при чём с каждой итерацией d уменьшается вдвое, пока не станет равен нулю

d = n // 2




#На вход массив arr {7, 6, 5, 4, 3, 2, 1}
#start - позиция, с которой нужно начать сдвигать элементы право на шаг step
#lastIndex - последняя позиция, которую надо сдвинуть вправо
#[start; lastIndex]
def shiftRight(arr, start, lastIndex, step):
    i = lastIndex
    while i >= start:
        arr[i + step] = arr[i]
        i -= step

#arr - исходный массив, который сортируем. start - индекс первого элемента, который будем сортировать.
#finish - индекс последнего элемента(не включительно). step - шаг, с которым мы будем просматривать элементы в списке, начиная со start
#Сортирует только один конкретный подмассив
def insertionSort(arr, start, finish, step):
    lastIndex = start + step
    while lastIndex < finish:
        cursor = lastIndex - step
        while (arr[cursor] > arr[lastIndex]) and (cursor != start):
            cursor -= step

        if (arr[cursor] > arr[lastIndex]) and (cursor == start):
            temp = arr[lastIndex]
            shiftRight(arr, 0, lastIndex - step, step)
            arr[cursor] = temp
        elif (arr[cursor] <= arr[lastIndex]):
            cursor += step
            temp = arr[lastIndex]
            shiftRight(arr, cursor, lastIndex - step, step)
            arr[cursor] = temp
        lastIndex = lastIndex + step


while d > 0:
    i = 0
    while i < d:
        insertionSort(arr, i, n, d)
        i += 1
    d = d //2


print('Массив после частичной сортировки ', arr)