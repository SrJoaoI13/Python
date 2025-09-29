frutas = ["Maca", "Abacaxi", "Banana", "Laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print()

frutas.append("Pera") 
print("Append: Adiciona um elemento ao final da lista.")
print(frutas) 
print()

frutas.insert(1,"Uva") 
print("Insert: Insere um elemento em uma posição específica da lista.")
print(frutas)
print()

frutas.remove("Banana") 
print("Remove: Remove a primeira ocorrência de um elemento na lista.")
print(frutas)
print()

frutas.pop(0) 
print("Pop: Remove e retorna o elemento em uma posição específica da lista.")
print(frutas)  
print()

frutas.sort() 
print("Sort: Ordena os elementos da lista em ordem ascendente.")
print(frutas) 
print() 

frutas.reverse() 
print("Reverse: Inverte a ordem dos elementos na lista..")
print(frutas)  