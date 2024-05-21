iphone = 0
samsung = 0
motorola = 0
count = 0
while count < 300:
    nome = input('qual seu nome? ')
    cidade = input('de que area voce é: ').lower()
    if cidade == 'iphone':
        iphone = iphone + 1
    elif cidade == 'samsung':
        samsung = samsung + 1
    elif cidade == 'motorola':
        motorola = motorola + 1
    count = count + 1

print(iphone, samsung, motorola)