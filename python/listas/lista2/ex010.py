lista = []
vogal = 0
consoante = 0
for i in range(10):
    valor = input('digite uma letra: ')
    lista.append(valor)
    if valor in ['a', 'e', 'i', 'o', 'u']:
        vogal = vogal + 1
    else:
        consoante = consoante + 1

print(vogal, consoante, lista)

