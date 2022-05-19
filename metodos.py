# listas arraws
from itertools import count


notas=[7.9, 9.7, 8.2]

lista=[]
lista=list()
lista=[29, 18,3.14, 20]

#Metodos

# 1-append
print('Antes:', lista)
lista.append(8)
print('Depois:', lista)

# 2-Insert
lista.insert(2, 16)
print('After insert:',lista)

# 3-extend
lista2=[1,2,3]
lista.extend(lista2)
print('After extend:', lista)

# 4-pop
lista.pop()
print('After pop:', lista)

lista.pop(0)
print('After pop:', lista)

# 5- remove
lista.remove(2)
print('After Remove:', lista)

# 6- Count
print('Quantidade de 2:', lista.count(1))

# 7- index
print('Index do elemento:', lista.index(16))

# 8- Sort
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

#Funcoes
# 1- Len
print(len(lista))

# 2- Sum
print(sum(lista))

# 3-Max
print(max(lista))

# 4- Min
print(min(lista))