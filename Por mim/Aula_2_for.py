"""For"""
print("==== For em Python ====")
print()
print("tem a função de repetir um bloco de código um número determinado de vezes")
for i in range(5):
 print ("O valor de i é: ", i)
print("Fim do laço for")

print()
print("tem a função de pular valores dentro do range usando o terceiro parametro do range")
for x in range(2, 11):
    print(x)

print()
print("tem a função de pular valores dentro do range usando o terceiro parametro do range")
for char in 'Python':
    print(char)

print()
print("lista é um vertor em python e pode ser percorrida com o for")
lista = [1, 2, 3, 4, 5, 6]
for i in lista:
    print(i)

print()
print("tem a função de percorrer uma lista de componentes de um computador")
cmputador = ['Mouse', 'Teclado', 'Monitor', 'Gabinete']
for item in cmputador:
    print("Componente: ",item)
