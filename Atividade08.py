lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

lista_produtos[1] = "rímel"
lista_produtos[4] = "cremes hidratantes"
lista_produtos.pop()

lista_produtos.append("cremes para massagem")
lista_produtos.append("condicionador")

for item in lista_produtos:
    print(f'Temos {item} à venda!')