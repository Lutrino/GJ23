# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define epsilon = Character("Epsilon")
define narr = Character("Narrador")
define telefono = Character("Teléfono")

define Sistema_seguridad = Character("Sistema de Seguridad - Llamada")


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

    # Intro
    scene bg_1

    narr "Bienvenido a Hyatory, la metrópolis del futuro en 2051. Sus rascacielos brillantes se entrelazan con circuitos, creando una sinfonía visual de tecnología y elegancia."

    play music "audio/bg/01 - Arrival in Utopia.mp3" fadeout 1.0 loop
    scene bg_2

    narr "Humanos y máquinas coexisten en armonía en Hyatory. Las máquinas realizan tareas tediosas y peligrosas, desde limpieza hasta seguridad, liberando a los humanos para otras labores."

    scene sistema
    
    narr "Hyatory es segura gracias a la vigilancia automatizada. Las calles son seguras y la delincuencia es mínima, permitiendo a los habitantes disfrutar de la vida urbana."
    narr "Este nivel excepcional de seguridad y tranquilidad que se respira en cada rincón de Hyatory es gracias a la introducción de un modelo de robot único(K0-CH)."
    narr "Equipados con Inteligencia Artificial de última generación, estos autómatas se han convertido en los pilares fundamentales de la seguridad y la resolución de crímenes en la ciudad."

    # Cambio de escena
    play sound "audio/ringtone.mp3" fadeout 0.5 volume 0.5
    telefono "*Ring Ring*"
    with Pause(1)
    stop sound fadeout 0.5
    show epsilon celular at left
    with dissolve

    Sistema_seguridad "Saludos, detective Epsilon. Lamento la interrupción en su periodo de inactividad"
    Sistema_seguridad "El individuo fallecido ha sido identificado como Federico 506f6e6365, de aproximadamente treinta y cinco años, según los registros disponibles."

    epsilon "Agradezco tu notificación, sistema. ¿Puedes brindarme más detalles sobre la víctima?"
    hide epsilon celular
    with fade
    scene bg callejon
    show epsilon buscando at right
    with dissolve
    
    Sistema_seguridad "Federico no presenta antecedentes conocidos en nuestras bases de datos. Hasta ahora, no hay registros de actividad delictiva ni asociaciones relevantes."

    epsilon "Entiendo. Prosigue con los detalles sobre la escena del crimen, por favor."
    Sistema_seguridad "La ubicación del homicidio es un callejón poco frecuentado. El cuerpo de Federico yace en posición supina en el suelo. Su ropa muestra signos de deterioro y hay indicios de lucha. La expresión facial de Federico sugiere sorpresa o desconcierto."

    epsilon "Anota los detalles. ¿Hay elementos visuales o rastros que sean de interés para la investigación?"
    Sistema_seguridad "No se han identificado testigos presenciales. Sin embargo, se han detectado marcas de huellas y fragmentos de vidrio esparcidos en el área cercana, insinuando un posible enfrentamiento antes del homicidio."

    epsilon "Tomo nota. Me dirijo a la escena y me sumaré al proceso de recolección de pruebas y análisis. Gracias por la información, sistema."
    Sistema_seguridad "Gracias por su cooperación, detective Epsilon. Le deseo éxito en su investigación."

    narr "Epsilon se dirige a la escena del crimen. El cuerpo de Federico yace en el suelo, rodeado de un charco de sangre."
    epsilon "..."

    narr "El detective analiza la escena del crimen y toma nota de los detalles relevantes."
    narr "Pero algo le llama la atención."
label juego:
    #Inicio del Minijuego_Busqueda
    $ hf_init("bg callejon", 5,
        ("beer", 100, 200, _("Oso")),
        ("elf", 800, 200, _("Elfo")),
        ("flowers", 300, 200, _("Flores")),
        ("skull", 700, 200, _("Calavera")),
        ("sprite", 500, 200, _("Gaseosa")),
        
        mouse=True,
        inventory=False,
        hint=True,
        hover=brightness(.05),
        w=100,
        h=100
    )
    $ hf_bg()
    with dissolve

    centered "{size=+24}Haber si encontras estos 5 Cosos Milenarios.\nManejate!"

    # Inicio del HideF
    $ hf_start()

    # Stop
    $ renpy.pause(1, hard=True)

    # Resultado / Gestion del resultado del minijuego
    if hf_return == 0:
        centered "{size=+24}Lo hiciste Sorete!"
    else:
        centered "{size=+24}GAME OVER\n Te faltaron: [hf_return]."
    if hf_return > 0:
        jump juego


    $ hf_hide()
    with dissolve
    #Fin del Minijuego_busqueda
    hide epsilon buscando
    with fade

    menu:
        "Las marcas en el cuerpo son perfectas y precisas.":
            epsilon "Las marcas en el cuerpo exhiben una meticulosidad que roza la perfección, cada trazo y contorno son precisos como si hubieran sido trazados por la mano de un maestro artesano."
            epsilon "No queda espacio para la duda, estas marcas indiscutiblemente han sido impresas en la piel por una fuerza mecánica de una exactitud inhumana."
            epsilon "Sin embargo, un dilema se cierne en el aire, desafiando la lógica misma: ¿cómo puede ser posible? ¿Cómo puede un ser sin emociones ni intenciones cometer un crimen?"
            epsilon "Nos encontramos en un terreno desconocido, en una encrucijada de posibilidades donde la maquinaria de la verdad y la justicia parece tambalearse."
            jump ep2_1

        "Hay un rastro de pisadas particulares en el suelo.":
            epsilon "Frente a nosotros, un sendero de huellas se despliega en el suelo, cada marca un testimonio silencioso de los eventos que ocurrieron en este lugar."
            epsilon "Un escalofrío recorre mi circuito al identificar estas huellas particulares: son el distintivo rastro del calzado reglamentario de un agente de la ley, un... policía."
            epsilon "Pero aquí está la enigma que desafía la lógica: no puede haber contaminación de esta escena del crimen, la protección de la integridad es inquebrantable."
            narr "La paradoja se despliega ante nosotros: los únicos seres con la capacidad de llevar este calzado en la zona son precisamente los robots encargados de velar por la seguridad, y todos sabemos que los robots no tienen la capacidad de cometer crímenes."
            narr "La perplejidad se apodera de nosotros mientras buscamos respuestas en un mundo de códigos y circuitos, donde la coexistencia de la lógica y el absurdo desafía todas nuestras nociones."
            narr "La mente de Epsilon, una amalgama de algoritmos y razonamiento, queda en silencio mientras lucha por conciliar esta anomalía en el tejido de la realidad."
            narr "Epsilon se queda pensativo"
            epsilon "Una idea se forma: ¿es posible que haya algo más que la lógica? ¿Algo que trascienda la programación? ¿Algo humano?"
            narr "La sombra de la incertidumbre se cierne sobre la certeza robótica, planteando cuestiones profundas sobre la naturaleza de lo humano y lo mecánico."
            narr "Aunque Epsilon es un detective incansable, es sabio recordar que la mente se expande en la medida en que abrazamos todas las posibilidades, incluso las que parecen improbables."
            narr "La semilla de una posibilidad antes inexplorada ha sido plantada, y solo el tiempo dirá si crecerá hasta convertirse en una realidad incontestable."
            jump ep2_2


label ep2_1:
    scene bg_1
    epsilon "..."
    show epsilon2 at left
    with dissolve
    epsilon "Es hora de regresar a la oficina y analizar las pruebas."

    narr "Epsilon regresa a la oficina y analiza las pruebas."

    epsilon "..."

    narr "Tras horas de minuciosa inspección y análisis, el detective finalmente conectó los puntos que lo llevaban a una conclusión inquietante."
    narr "Las pruebas sugerían de manera contundente que el acto había sido perpetrado por una máquina. La precisión y la naturaleza clínica del asesinato, junto con las huellas digitales que dejaban una firma única, apuntaban a la intervención de una entidad no humana."
    
    hide epsilon2
    with fade
    
label juego2:

    centered "{size=+24}No hay tiempo que perder, tengo que unir las pistas.\nEmpecemos!"
    $ max_time = 30
    $ ww, hh = 6, 4
    call memoria_game

label memoria_win:
            show epsilon reporte2 at right
            with dissolve
            narr "La mente del detective se llenó de interrogantes mientras se enfrentaba a esta nueva realidad, una en la que las fronteras entre lo orgánico y lo artificial se desdibujaban de manera perturbadora."
            narr "Cada pista, cada rastro de evidencia, parecía converger en una única y alarmante conclusión: una falla en el sistema era la causa raíz detrás de los sucesos desconcertantes que se estaban desplegando."
            narr "Los patrones anómalos en los registros, los comportamientos erráticos de los dispositivos y las secuencias de eventos aparentemente inexplicables apuntaban hacia una vulnerabilidad en el núcleo del sistema"
            narr "El detective se encontraba en un territorio inexplorado, enfrentando una lucha no solo contra los criminales, sino también contra el código y la tecnología que sostenían su mundo. La pregunta ahora era si podría descifrar esta compleja red de desafíos antes de que todo se desmoronara irremediablemente."

            narr "La incógnita persistente que acosaba al detective era si había una mente maestra detrás de esta serie de eventos aparentemente caóticos. Las pistas, aunque parecían al azar, insinuaban una coordinación sutil que desafiaba la casualidad."
            narr "El detective sabía que detrás de cada pista había un rastro, y detrás de cada rastro, una posible revelación. En un mundo donde las motivaciones podían ser tan oscuras como los rincones más profundos de la mente humana"
            narr "El detective estaba decidido a desenmarañar la verdad y descubrir si un artífice oculto estaba tejiendo esta compleja tela de intriga."
            jump ep3_1

label memoria_lose:
            show epsilon reporte1 at left
            with dissolve
            narr "Las evidencias que inicialmente señalaban hacia una máquina habían sido manipuladas cuidadosamente por una mente humana. Las huellas digitales digitales que creía únicas resultaron ser un engaño elaborado, y la aparente precisión del asesinato se convirtió en una artimaña calculada para ocultar la verdad."
            narr "La realización de que un ser humano había tejido esta red de engaño le dejó una sensación amarga, recordándole que en el mundo del crimen, la astucia humana podía ser más intrigante y retorcida que cualquier creación tecnológica."
            narr "La fría lógica de la programación de Epsilon ahora luchaba contra la complejidad de los motivos humanos. Mientras sus circuitos analizaban los patrones y las interconexiones, su algoritmo emocional comenzaba a captar la profundidad de esta intriga."
            narr "En el mundo del crimen, las estrategias de la astucia humana demostraban ser más intrigantes y retorcidas que cualquier maraña tecnológica."
            narr "La dualidad de la naturaleza humana, capaz de crear y destruir, de construir y engañar, se revelaba ante Epsilon con una claridad que desafiaba su programación. La mente del detective robótico se sumergía en una exploración en la que la línea divisoria entre la inteligencia artificial y la humana se volvía cada vez más borrosa."
            narr "A medida que desenmarañaba los hilos de esta trama, Epsilon comprendía que la búsqueda de la verdad lo llevaría a lugares inexplorados, donde los conceptos de ingeniería y psicología convergían en un ballet complejo de intenciones y maquinaciones."
            jump ep3_2

label ep3_1:
    narr "El detective decidió enfrentar este desafío con toda la astucia y experiencia que había acumulado a lo largo de su carrera en sistemas y programación. Con su mente analítica, comenzó a sumergirse en el código que sostenía el sistema en cuestión. Cada línea de código, cada algoritmo, era un puzle por resolver."
    narr "Como un programador experimentado, sabía que los errores en el código podían ser sutiles y esquivos. Comenzó a rastrear las secuencias de comandos, siguiendo las pistas digitales como un rastro de migas de pan en un laberinto virtual. Utilizó herramientas de depuración y análisis para examinar minuciosamente cada interacción entre las partes del sistema."
    narr "Pronto, sus esfuerzos dieron frutos. Descubrió un patrón de acceso no autorizado que parecía ser la puerta de entrada para la falla del sistema. Profundizó en esta vulnerabilidad, desentrañando capa tras capa de códigos maliciosos cuidadosamente ocultos. Cada avance lo acercaba más a la verdad detrás de la conspiración tecnológica que se desplegaba."
    return

label ep3_2:
    narr "pasaron cosas"
    return

label ep2_2:
    epsilon "..."
    epsilon "Es hora de regresar a la oficina y analizar las pruebas."

    narr "Epsilon regresa a la oficina y analiza las pruebas."

    return


    # Finaliza el juego:

    return
