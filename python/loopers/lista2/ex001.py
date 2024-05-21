i = 0
sexom = 0 
sexof = 0

while i < 10:
    nome = input('escreva seu nome: ')
    sexo = input('escreva seu sexo [(F) ou (M)]').upper()
    if sexo == 'F':
        sexof = sexof + 1
    elif sexo == 'M':
        sexom = sexom + 1
    i = i + 1
    print(i)

print(sexom, sexof)