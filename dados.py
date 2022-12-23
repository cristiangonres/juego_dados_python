from random import randint
from time import sleep

#JUEGO ADIVINAR EL NÚMERO DE LOS DADOS
dados_valor = {}
#Dibujo dado en lista
dado_dibujo = ['''
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
def lanzar_dados(n_dados):
    suma_valores = 0
    #Crear diccionario con dados y valores aleatorios
    for i in range(1, n_dados+1):
        dados_valor['dado'+str(i)] = randint(1,6)
    #Imprimir dados    
    for dado, valor in dados_valor.items():
        print(f'El dado {dado[4:5]} tiene un valor de {valor}:' )
        print(f'{dado_dibujo[valor-1]} \n\n')
        suma_valores += valor       
         
    return suma_valores

def evaluar_jugada(numero, suma_dados):
    
    if suma_dados == numero:
        return f"Genial, has acertado, el resultado es: {suma_dados}. ERES MUY AFORTUNADO"
    else:
        return f"La fortuna no te sonrie, el resultado era: {suma_dados}. SIGUE PROBANDO"

numero = 0
n_dados = int(input('¿Cuántos dados vas a lanzar? '))

while numero not in range(1, n_dados*6+1):
    numero = int(input('Intenta adivinar el número que vas a sacar (la suma de los dos dados): '))
    if numero not in range(1, n_dados*6+1):
        print(f'El valor debe estar entre 1 y {n_dados*6}')
print('Lancemos los dados...')
sleep(1)
print('.')
sleep(1)
print('..')
sleep(1)
print('...')
sleep(1)

print(evaluar_jugada(numero, lanzar_dados(n_dados)))