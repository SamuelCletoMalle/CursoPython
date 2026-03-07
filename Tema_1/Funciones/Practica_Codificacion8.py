""" Enunciado

Escribe un programa en Python que contenga una función llamada generar_mensaje para crear mensajes personalizados.

Incluye un docstring al inicio de la función que describa su propósito, los parámetros que toma y lo que devuelve.

La función debe recibir dos argumentos:

nombre (argumento posicional). El nombre de una persona.

mensaje (parámetro con valor por defecto, "Bienvenido al curso de Python").

La función debe crear y devolver un mensaje completo utilizando la sentencia return, combinando el nombre y el mensaje predeterminado. Asegúrate de que el docstring refleje esta funcionalidad.

Después de definir la función, realiza una llamada a generar_mensaje con un nombre específico y muestra el resultado.



Resultado esperado

"¡Hola, Santiago! Bienvenido al curso de Python" """

def generar_mensaje(nombre, mensaje="Bienvenido al curso de Python"):


    """
    Genera un mensaje personalizado de bienvenida.

    Parámetros:
    nombre (str): Nombre de la persona a la que se dirige el mensaje.
    mensaje (str, opcional): Mensaje de bienvenida. Por defecto es
    "Bienvenido al curso de Python".

    Devuelve:
    str: Un mensaje completo que combina el saludo con el nombre de la
    persona y el mensaje de bienvenida.
    """
    return f"¡Hola, {nombre}! {mensaje}"


resultado = generar_mensaje("Samuel")
print(resultado)