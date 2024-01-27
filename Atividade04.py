nome = input('informe seu nome completo: ')
ano = int(input('informe o ano em que nasceu: '))


while ano < 1922 or ano > 2021:
    ano = int(input('Informe um ano válido: '))
    

print(f'olá {nome}, você fará {2022 - ano} anos de idade em 2022 (ano atual).')