"""
Somatório de duas lista com indices de tamanhos diferentes, utilizar
todos os métodos conhecidos.
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

# Soma utilizando for + zip
for a, b in zip(lista_a, lista_b):
    lista_soma.append(a + b)
print(lista_soma)

# Soma utilizando list comprehension
somatorio = [(a+b) for a, b in zip(lista_a, lista_b)]
print(somatorio)

# Soma utilizando for, range
lista_soma = []
t = len(lista_b)
for i in range(t):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# Soma utilizando while
lista_soma, a = [], 0
while a < t:
    b = lista_a[a] + lista_b[a]
    lista_soma.append(b)
    a += 1
print(lista_soma)