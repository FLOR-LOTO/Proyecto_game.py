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

words = ['alambre', 'martillo', 'armario', 'elefante', 'camisa', 'empaquetar', 'alcohol', 'amor', 'tigre', 'salamandra']

#Bienvenida
welcome = lambda:print('Bienvenido al juego: "EL AHORCADO"\n'
      '\n'
      'OBJETIVO DEL JUEGO:\n'
      'Debes adivinar la palabra oculta.\n'
      '\n'
      'CÓMO JUGAR:\n'
      '1. Tienes 5 oportunidades para adivinar la palabra.\n'
      '2. Ingresa una letra cada vez.\n'
      '3. Si la letra está en la palabra, se mostrará su posición.\n'
      '4. Si la letra no está, perderás una oportunidad.\n'
      '5. Si pierdes todas las oportunidades, tendrás que empezar de nuevo.\n'
      '\n'
      '🍀¡Buena suerte!🍀\n')

#logica para restar vidas
def lifes(count, acert):
    if not acert:
        count -= 1
        print(f'Haz perdido una oportunidad 😟, tienes {count} vidas restantes')
        print('\n')
    else:
        print('Felicitaciones, haz acertado la letra, sigue así 🤩')
        print('\n')
        
    if count == 0:
        print('Ya no tienes vidas 😭')
        print('\n')
        
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
    
    return new_word.upper()


def start_game():
    random_word = random.choice(words).upper() #random_word guarda la palabra escondida
    correct_letters = set()            #almacena las letras que el jugador ha adivinado correctamente, un set()evita duplicados
    incorrect_letters = []             #guarda las letras erroneas
    lives = 5                          #vidas iniciales
    word_length = len(random_word)     #cantidad de letras
    
    welcome()
    
    print(f'LA PALABRA CONTIENE {word_length} LETRAS' '\n')
    
    while lives > 0: 
        """
        bucle que ejecutará la dinamica, si tengo al menos una vida entra nuevamente en el bucle
        muestra la palabra oculta con las letras acertadas al momento
        pide el ingreso del caracter y lo guardo en una variable
        """            
        print('Decifrado hasta el momento: ' + word_incognit(random_word, correct_letters))
        print('-----------------------------------------------')
        char_params = input('Elije una letra: ')
        print('\n')
        char_param = char_params.upper()
        
        if not isinstance(char_param, str) or len(char_param) != 1 or not char_param.isalpha(): 
            """
            si no es un string o es un número o caracter especial da error pero contínua con el bucle
            continue permite Volver al inicio del bucle while, pidiendo una nueva letra hasta que sea un caracter válido
            """
            print("ERROR ❌: El dato debe ser una letra.")
            print('\n')
            continue
    
        if char_param in correct_letters or char_param in incorrect_letters:
            """
            verifico si ya se uso la letra tanto en el conjunto de acertadas como de erroneas
            continue permite Volver al inicio del bucle while, pidiendo una nueva letra hasta que sea un caracter válido
            """
            print(f'Ya has intentado con la letra "{char_param}". Intenta con otra🤞')
            print('\n')
            continue
        
        if char_param in random_word:
            """
            verifico si la letra esta en la palabra y la sumo a las letras adivinadas add por que es un set
            verifico si todas las letras fueron adivinadas, si es así finalizo el bucle (break)
            Si la letra no esta en la palabra, la sumo a la lista de incorrectas append por que es una list y resto una vida
            si las vidas son igual a cero, termino el bucle (break)
            """
            correct_letters.add(char_param)
            print(f'¡Bien hecho 👍! La letra "{char_param}" está en la palabra.')
            print('\n')
            
            if set(random_word) == correct_letters:
                print(f'¡Felicidades 🥳! Has descubierto la palabra: {random_word}')
                print('\n')      
                break
        else:
            incorrect_letters.append(char_param)
            print(f'LETRAS ERRÓNEAS HASTA EL MOMENTO: {incorrect_letters}')
            print('\n')
            lives = lifes(lives, False)
        
        if lives == 0:
            print(f'La palabra oculta era: {random_word}')
            print('\n')
            break
    """
    opción de comenzar un nuevo juego con recursión
    """
    if input('¿QUIERES INTENTAR DE NUEVO? (s/n): ').lower() == 's':
        start_game()

start_game()