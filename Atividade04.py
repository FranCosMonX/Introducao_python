nome = input('informe seu nome completo: ')
ano = 0

while ano < 1922 or ano > 2021:
    try:
        ano = int(input('Informe um ano válido: '))
    except:
        print('É aceito apenas número inteiro. Por favor, tente novamente.')

print(f'olá {nome}, você fará {2022 - ano} anos de idade em 2022 (ano atual).')