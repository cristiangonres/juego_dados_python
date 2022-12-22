from random import randint
from time import sleep

#Dibujo dado en lista

dado = ['''
 ___________
|           |
|           |
|     *     |
|           |
|___________|
''', '''
 ___________
|           |
|       *   |
|           |
|    *      |
|___________|
 ''', '''
 ___________
|           | 
|       *   |
|     *     |
|   *       |
|___________|''', '''
 __________
|          |
|  *    *  |
|          |
|  *    *  |
|__________|''', '''
 ___________
|           |
|  *     *  |
|     *     |
|  *     *  |
|___________|''', '''
 ___________
|           |
|  *  *  *  |
|           |
|  *  *  *  |
|___________|''']

#obtener dos números aleatorios
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print(f'PRIMER DADO: {dado1} {dado[dado1-1]}\n')
    print(f'SEGUNDO DADO: {dado2} {dado[dado2-1]} \n\n')
    
    return dado1, dado2

def evaluar_jugada(dado1, dado2, numero):
    suma_dados = dado1 + dado2
    if suma_dados == numero:
        return f"Genial, has acertado, la suma de los dados es {suma_dados}"
    else:
        return f"La fortuna no te sonrie, la suma de los dados es {suma_dados}"

numero = 0
while numero not in range(1, 12):
    numero = int(input('Intenta adivinar el número que vas a sacar (la suma de los dos dados): '))
    if numero not in range(1, 12):
        print('El valor debe estar entre 1 y 12')
print('Lancemos los dados...')
sleep(1)
print('.')
sleep(1)
print('..')
sleep(1)
print('...')
sleep(2)
dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2, numero))