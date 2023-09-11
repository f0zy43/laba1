import statistics
import re

print('Вводите значения')
print('для окончания ввода напишите end')
A = []
num = int(input('-->>'))

while True:
    A.append(num)
    num = input('-->>')
    if num == 'end':
        break
    try:
        num = int(num)
    except ValueError:
        print('Ошибка. Введите правильно')
        continue

print(A)
print(f'Максимальное:{max(A)}')
print(f'Минимальное: {min(A)}')
print(f'Среднне: {statistics.mean(A)}')
print(f'Отклонение: {statistics.stdev(A)}')
