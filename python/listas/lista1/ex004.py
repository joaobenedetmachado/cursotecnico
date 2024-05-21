letras = vog = con = []

for i in range(0, 6):
    carac = input('digite uma letra: ')
    if carac in ['a', 'e', 'i', 'o', 'u']:
        vog.append(carac)
    else:
        con.append(carac)
        
print(vog, con)