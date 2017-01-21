import ptvsd
ptvsd.enable_attach('xplatform')

import random
cuenta_intentos = 0
nombre = input('Hola! Cual es tu nombre?\n')
numero = random.randint(1, 20)
print('Bienvenido, {0}. Adivina el numero (entre 1 y 20): '.format(nombre))

while cuenta_intentos < 6:
    intento = int(input('Haz un intento: '));
    cuenta_intentos += 1
    
    if abs(intento - numero) > 3:
        print('Lejos')
    elif abs(intento - numero) > 1:
        print('Cerca')
    else:
        break

if intento == numero:
    print('Excelente {0}, adivinaste el numero en {1} intentos'.format(nombre, cuenta_intentos))
else:
    print('Perdiste! El numero era {0}'.format(numero))