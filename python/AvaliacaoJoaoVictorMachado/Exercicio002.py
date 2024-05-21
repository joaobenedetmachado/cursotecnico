# João Victor Benedet Machado - 1190

data = str(input('Escreva uma data no formato (DD/MM/AAAA): ')).replace('/', ' ')

dia = int((data.split())[0])
mes = int((data.split())[1])
ano = (data.split())[2]

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and len(ano) == 4 and int(ano) >= 1:
    print(f'A data {data.replace(' ', '/')}, é valida.') 
else:
    print(f'A data {data.replace(' ', '/')}, é valida.') 
