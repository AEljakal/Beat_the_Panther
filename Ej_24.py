import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "juego", "ahorcado", "computadora"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    for letra in palabra:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("La palabra tiene", len(palabra_secreta), "letras.")

    while intentos_restantes > 0:
        print("Intentos restantes:", intentos_restantes)
        mostrar_palabra(palabra_secreta, letras_adivinadas)

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has ingresado esa letra. ¡Intenta con otra!")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! Has adivinado una letra.")
        else:
            print("¡Incorrecto! Esa letra no está en la palabra.")
            intentos_restantes -= 1

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break

    if intentos_restantes == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra era:", palabra_secreta)

# Ejecutar el juego
jugar_ahorcado()
