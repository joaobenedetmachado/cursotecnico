cont = total = media = 0
while cont < 10:
    numero = int(input('escreva um numero:'))
    cont = cont + 1 
    total = total + numero
    media = (total)/cont
    
print(media, total)