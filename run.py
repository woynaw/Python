print("Введите n")
n = int(input())
print("Введите m")
m = int(input())
print("Введите элементы первого массивa")
a = []
b = []
for i in range(n):
    a.append(int(input()))
print("Введите элементы второго массивa")
for i in range(m):
    b.append(int(input()))
c = a + b
for i in range(0, len(c) - 1):
    min = i
    for j in range(i + 1, len(c)):
        if c[j] < c[min]:
            min = j
    c[i], c[min] = c[min], c[i]
c = set(c)
print(*c)
