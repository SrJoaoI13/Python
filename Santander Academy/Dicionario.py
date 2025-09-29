pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"
print()

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print("keys(): retorna uma visualização de todas as chaves do dicionário.")
print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print()
print("values(): retorna uma visualização de todos os valores do dicionário.")
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print()
print("items(): retorna uma visualização de todos os pares chave-valor do dicionário.")
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])
print()
print("update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.")
pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}