lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

#Ah duas formas de fazer

# >> primeira
print("primeira maneira:")
for i in range(len(lista_produtos)):# de i até a qtd limite de itens da lista, faça...
    print(f'Temos {lista_produtos[i]} à venda!')

# >> segunda
print("\nsegunda maneira:")
for item in lista_produtos: #para cada item da lista, faça
    print(f'Temos {item} à venda!')