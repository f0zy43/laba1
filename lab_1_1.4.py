a = 0
b = 2500

A = []

for x in range(a+1, b):
   if x % 10 == 1:
      b = x ** 2
      A.append(b)
print(A)
