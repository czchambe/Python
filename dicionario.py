#dicionario
dicionario ={}
dicionario=dict()
dicionario={'nome':'Chambe', 'idade':29, "altura":1.90}
print(dicionario)
print(dicionario['nome'])

# adicionar elementos no dicionario
dicionario["programador"]=True
print(dicionario)
dicionario["idade"]=30
print(dicionario)

# Percorer dicionario

for i in dicionario:
    print(i)

for i in dicionario:
    print(i,dicionario['nome'])

#Testanto a existencia de chaves
print("peso" in dicionario)
print("idade" in dicionario)

