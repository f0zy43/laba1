from random import randint
 
def bubble(array): #пузырьком
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

def shell_sort(array): # сортировка шелла
    gap = len(array) // 2

    while gap > 0:
        for value in range(gap, len(array)):
            current_value = array[value]
            position = value

            while position >= gap and array[position - gap] > current_value:
                array[position] = array[position - gap]
                position -= gap
                array[position] = current_value

        gap //= 2
    return array

def insertion_sort(array): #вставками
    for item in range(1, len(array)):
        current_value = array[item]
        position = item

        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_value

    return array

def merge_sort(array): #сортировка слиянием
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_list = array[:middle]
    right_list = array[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))


def merge(left_half, right_half): # для сорт слиянием
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res += right_half
    else:
        res += left_half
    return res

def quick_sort(array): # юыстрая сортировка
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, low, high):
    if low < high:
        split_point = partition(array, low, high)
        quick_sort_helper(array, low, split_point - 1)
        quick_sort_helper(array, split_point + 1, high)


def partition(array, low, high):
    pivot_value = array[low]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and array[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]

    array[low], array[right_mark] = array[right_mark], array[low]
    return right_mark
 
N = int(input('Размер массива:'))
a = []
for i in range(N):
    a.append(randint(1, 99))

print("исходный массив:")
print(a)
print("Сортировка пузырьком:")
bubble(a)
print(a)
print("Сортировка шелла:")
shell_sort(a)
print(a)
print("Сортировка вставками:")
insertion_sort(a)
print(a)
print("Сортировка слиянием:")
merge_sort(a)
print(a)
print("Быстрая сортировка:")
quick_sort(a)
print(a)