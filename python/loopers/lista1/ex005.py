total = total = media = count = 0
while True:
    numero = int(input('digite um numero: '))
    if numero > 1:
        total = total + numero
        count = count + 1
        media = (total)/count
    if numero < 1:
        print(media)
        print(total)
        break
