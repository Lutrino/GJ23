﻿# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

define started = False

# El juego comienza aquí.

label splashscreen:
    scene black
    with Pause(1)

    play music "audio/MUSIC02.mp3" fadeout 1.0 noloop

    show text "KochCorp Presents..." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    $ started = True
    return

label start:

    stop music fadeout 1.0

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
