i = 0 
maior = 0
menor = 0
while i < 10:
    i = i + 1
    numero = int(input('DIGITE UM NUMERO: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(maior, menor)

