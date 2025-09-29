conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print("Retorna um novo conjunto contendo todos os elementos que estão em conjunto1 ou em conjunto2 (ou em ambos).")
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print("retorna um novo conjunto contendo apenas os elementos que estão em ambos os conjuntos.")
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print("Retorna todos os elementos que estão em conjunto1 mas não estão em conjunto2.")
print(diferenca)  # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print("Retorna todos os elementos que estão em um conjunto ou no outro, mas não em ambos.")
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

print()
frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print("Add(elemento): adiciona um elemento ao conjunto.")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print("Remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print("Discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print("Clear(): remove todos os elementos do conjunto.")
print(frutas)  # Imprime set()