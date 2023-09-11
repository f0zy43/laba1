a = 0
b = 2500

for x in range(a, b):
    if x % 2 == 5 and (x**2)%2 == 5:
        print([x for x in range(a, b)])
