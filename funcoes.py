# Criar funcoes

def saudacao():
    print("Seja bem vindo(a)")
    print("Olá é um prazer")

saudacao()

# Funcao recebendo parametros
def saudacao(nome):
  print(f'Seja bem vindo(a), {nome}')
  print("Olá é um prazer")

saudacao("Chambe")

def saudacao(nome,curso):
  print(f'Seja bem vindo(a), {nome}')
  print(f"Olá é um prazer programar em: {curso}")

saudacao("Chambe","Python")

# Funcao com parametros default
def saudacao(nome,curso="PHP"):
  print(f'Seja bem vindo(a), {nome}')
  print(f"Olá é um prazer programar em: {curso}")

saudacao("Chambe")

# Funcao com retorno
def soma (num1, num2):
    return num1+num2
resultado= soma(8,8)
print("Resultado", resultado)

def calculadora (num1, num2, operacao='+'):
     if operacao=='+':
         return num1+num2
     elif operacao=='-':
         num1-num2
resultado=calculadora(10, 20)
print(resultado)

