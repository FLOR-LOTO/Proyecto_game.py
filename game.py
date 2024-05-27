"""
El objetivo consiste en desarrollar el juego interactivo “adivina la palabra”.
El funcionamiento esperado es el siguiente:
Al ejecutar el programa se mostrará por pantalla una palabra oculta usando tantos guiones
como letras contiene la palabra a adivinar(la palabra a adivinar será elegida por el
programa usando el módulo de Python random), la cantidad de vidas con las que cuenta el
jugador y las cantidad de letras incorrectas que va ingresando.
Cuando el jugador ingresa una letra es necesario que se valide el dato( que sea una letra).
Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a alguna de
las letras de la palabra a adivinar.
Cada vez que el jugador ingrese una letra que NO pertenece a la palabra a adivinar se
restará una vida.
El juego finaliza cuando el jugador queda sin vidas o cuando adivina todas las letras de la
palabra. Para todos los casos se debe mostrar un mensaje indicando si ganó la partida o si
perdió. 
"""
import random

words = ['alambre', 'martillo', 'armario', 'elefante', 'camisa', 'empaquetar', 'alcohol']

#Bienvenida
welcome = lambda:    print('Bienvenido al juego: "EL AHORCADO"\n'
      '\n'
      'Objetivo del juego:\n'
      'Debes adivinar la palabra oculta.\n'
      '\n'
      'Cómo jugar:\n'
      '1. Tienes 5 oportunidades para adivinar la palabra.\n'
      '2. Ingresa una letra cada vez.\n'
      '3. Si la letra está en la palabra, se mostrará su posición.\n'
      '4. Si la letra no está, perderás una oportunidad.\n'
      '5. Si pierdes todas las oportunidades, tendrás que empezar de nuevo.\n'
      '\n'
      '❤❤❤❤❤❤¡¡¡Mucha suerte!!!❤❤❤❤❤❤\n')

#logica para restar vidas
def lifes(count, acert):
    if not acert:
        count -= 1
        print(f'Haz perdido una oportunidad, tienes {count} vidas restantes')
    else:
        print('Felicitaciones, haz acertado la letra, sigue así')
        
    if count == 0:
        print('Ya no tienes vidas. Vuelve a comenzar el juego')
        
    return count

# Crear una nueva palabra donde los caracteres no presentes en la palabra son reemplazados por '-'
def word_incognit(word, visible_character):
    """
    word: La palabra que queremos transformar.
    visible_character: Caracteres(lista) que deben ser visibles en la nueva palabra, mientras que los otros caracteres serán reemplazados por guiones (-).
    """
    new_word = []
    
    for char in word:
     if char in visible_character:
        new_word.append(char)
     else:
        new_word.append('-')
        
    new_word = ''.join(new_word) #convertimos el resultado de elementos de new_word a una sola string ''.join


def start_game():
    random_word = random.choice(words) #random_word guarda la palabra escondida
    correct_letters = set()            #almacena las letras que el jugador ha adivinado correctamente, un set()evita duplicados
    incorrect_letters = []             #guarda las letras erroneas
    lives = 5                          #vidas iniciales
    word_length = len(random_word)     #cantidad de letras
    
    welcome()
    
    print(f'LA PALABRA CONTIENE {word_length} LETRAS')
    
    
start_game()