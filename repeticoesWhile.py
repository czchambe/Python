#repeticoes

numero_sorteado =15
numero_escolhido=int(input("Digite um numero de 1 a 20:"))

"""
if numero_sorteado==numero_escolhido:
    print("Errado")
else:
    print("Certo")
"""
while numero_escolhido != numero_sorteado:

    print("Errado, tente novamente...")
    numero_escolhido=int(input("Digite um numero de 1 a 20:"))
print("Certo")

contador=0
while contador<5:
    print(contador)
    contador=contador+1
    