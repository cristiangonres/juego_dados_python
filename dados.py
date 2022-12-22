from random import randint

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

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"Tu puntuación es {suma_dados}. Lamentable"
    elif suma_dados >=10:
        return f"Tu puntuación es {suma_dados}. Tienes buena suerte!!"
    else:
        return f"La fortuna no te sonrie, has sacado {suma_dados} puntos"
    
dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))