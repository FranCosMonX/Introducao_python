def calculadora (a : float , b : float , op : str):
  if op == "+": return a + b
  elif op == "-": return a - b
  elif op == "*": return a * b
  elif op == "/":
    if b == 0: return 0
    else: return a / b
  else: return 0

def programa():
    strMenu = ("Menu:\n" +
        "1 - soma\n" +
        "2 - subtração\n" +
        "3 - multiplicação\n" + 
        "4 - divisão\n" +
        "0 - sair\n" +
        "R: "
        )
    
    escolha : int = -1
    while escolha != 0:
      escolha = int(input(strMenu))
      
      if (escolha < 5) and (escolha > 0):
        a = float(input("Informe o primeiro valor: "))
        b = float(input("Informe o segundo valor: "))
        
        resposta : float
        if escolha == 1:
          resposta = calculadora(a,b,"+")
        elif escolha == 2:
          resposta = calculadora(a,b,"-")
        elif escolha == 3:
          resposta = calculadora(a,b,"*")
        else:
          resposta = calculadora(a,b,"/")
          
        print(f'Resposta = {resposta}')
        
    print("Programa executado com sucesso!")

programa()