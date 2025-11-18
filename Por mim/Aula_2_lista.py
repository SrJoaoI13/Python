"""Lista"""
print()
print("==== Lista em Python ====")
print()
print(" Tem a função de armazenar múltiplos valores em uma única variável")
lista = [10, 20, 30, 40, 50, 756, 808, 909, 1001]
print(lista[4])  # Acessa o quinto elemento da lista
print()
print(" Tem a função de retornar o tamanho da lista")
print(len(lista))  # Retorna o tamanho da lista
print()
print(" Tem a função de adicionar um elemento ao final da lista")
lista.append(606)  # Adiciona um elemento ao final da lista
print(lista)
print()
print(" Tem a função de inserir um elemento em uma posição específica da lista")
lista.remove(30)  # Remove o elemento 30 da lista
print(lista)
print()
print(" Tem a função de remover um elemento específico da lista usando o índice")
lista.pop(2)  # Remove o elemento no índice 2
print(lista)
print()
print(" Tem a função de remover um elemento específico da lista usando o índice")
del lista[5]  # Remove o elemento no índice 4
print(lista)
print()
print(" Tem a função de limpar todos os elementos da lista")
lista.clear()  # Remove todos os elementos da lista
print(lista)

