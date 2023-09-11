a = 0
b = 2500

A = []

for x in range(a+1, b):
   if x % 10 == 1:
      c = x ** 2
      A.append(c)
print(A)
