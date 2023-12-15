print("resposta da questão")
for i in range(0, 20):
 if i == 12:
  continue
 print(i + 1)

print("usando while()")
contador : int = 0
while(contador < 20):
 contador += 1
 if contador == 13:
  continue
 print(contador)

print("questão desafio")
for x in range (20, 0, -1):
 if x == 13:
  continue
 print(x)