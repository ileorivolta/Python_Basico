import random

def run():
    numerorandom = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    vidas = 5

    while numerorandom != numero_elegido:
        
        if numero_elegido < numerorandom:
            print('Es un numero mas grande')
            vidas -= 1
            print('te quedan:', vidas, 'vidas')
        elif numero_elegido > numerorandom:
            print('Es un numero mas pequeño')
            vidas -=1
            print('te quedan:', vidas, 'vidas')
        if vidas == 0:
            print('GAME OVER, suerte a la proxima crack')
            break
        numero_elegido = int(input('Elige otro numero: '))

    if numero_elegido == numerorandom:
            print('GANASTE!, khe grande')
        
    print('Termino el juego')



if __name__ == '__main__':
    run()