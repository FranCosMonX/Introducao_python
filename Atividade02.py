def operacao (a : int , b : int , op : str):
  if op == "+": return a + b
  elif op == "-": return a - b
  elif op == "*": return a * b
  elif op == "/":
    if b == 0: return 0
    else: return a / b
  else: return 0
  
resultado = operacao(2,0,"/")
print(f'resultado da divisão: {resultado}')
resultado = operacao(2,6,"/")
print("resultado da divisão: {}".format(resultado))
print("resultado anterior com arredondamento: {:.2}".format(resultado))
resultado = operacao(2,6,"+")
print("resultado da soma: ", resultado)