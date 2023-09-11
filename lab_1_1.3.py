n = int(input('Размер списка:'))

dictionary = dict(input("Введите ключ и значение:").split() for _ in range(n))
result = "".join(f"{key}{value}" for key, value in dictionary.items())
result2 = "".join(f"{value}" for key, value in dictionary.items())

print(dictionary)
print(result)
print(result2)