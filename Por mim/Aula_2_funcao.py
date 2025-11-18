import random
import math
import datetime

print()
def imprimir():
    print("Função sem parâmetro")
    print("Outra linha dentro da função")
imprimir()

print()
def somar(a, b):
    return a + b
print("Chamando a função somar:")
print(somar(3, 5))

print()
def multiplicar(x,y):
    resultado = x * y
    print(resultado)
print("Chamando a função multiplicar:")
print(multiplicar(4, 6))

print()
print("Importando módulo random:")
print(random.randint(1, 100))  # Gera um número aleatório entre 1 e 100

print()
print("Importando módulo math:")
print(math.sqrt(16))  # Calcula a raiz quadrada de 16

print()
print("Importando módulo datetime:")
print(datetime.datetime.now())  # Exibe a data e hora atual
agora = datetime.datetime.now()
print(agora.year)