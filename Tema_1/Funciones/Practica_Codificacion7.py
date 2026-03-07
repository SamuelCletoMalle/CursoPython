""" Crea una función llamada organizar_fiesta: Esta función representará la organización de una fiesta de cumpleaños. La función debe tener tres argumentos:

invitados (argumento posicional): Un número entero que indica cuántos invitados asistirán.

tema (argumento de palabra clave con valor por defecto): Una cadena de texto que representa el tema de la fiesta. El valor por defecto debe ser "Python".

lugar (argumento de palabra clave con valor por defecto): Una cadena de texto que indica dónde se celebrará la fiesta. El valor por defecto debe ser "aula de informática".

Dentro de la función organizar_fiesta:

Imprime un mensaje que diga: "Preparando una fiesta para [invitados] invitados."

Imprime otro mensaje que diga: "Tema de la fiesta: [tema]"

Finalmente, imprime: "Lugar de la celebración: [lugar]"

Prueba la función con diferentes argumentos:

Llama a la función proporcionando solo el número de invitados.

Llama a la función proporcionando solo el número de invitados y el tema de la fiesta.

Llama a la función proporcionando todos los argumentos.



Resultado esperado

Preparando una fiesta para 10 invitados.

Tema de la fiesta: Python

Lugar de la celebración: aula de informática"""

def organizar_fiesta(invitados, tema="Python", lugar="aula de informática"):
    print(f"Preparando una fiesta para {invitados} invitados.")
    print(f"Tema de la fiesta: {tema}")
    print(f"Lugar de la celebración: {lugar}")
    print()  



organizar_fiesta(10)


organizar_fiesta(15, tema="Superhéroes")


organizar_fiesta(20, tema="Videojuegos", lugar="salón de eventos")




