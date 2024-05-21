numero = '101001'

numeroinverso = numero[::-1]
numeros = []
print(numeroinverso)

for i in range(0, len(numeroinverso)):
    if numeroinverso[i] == '1':
        print(2**i)
        
