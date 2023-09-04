num = int(input('Digite um numero '))
cont = 0
for i in range(num):
  if (num%(i+1) == 0):
    cont = cont + 1
    
if (cont==2):
 print('Ele é um numero primo')
else:
  print('Ele não é um numero primo')
