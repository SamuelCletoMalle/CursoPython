"""Función para contar caracteres en una cadena:

Define una función llamada contar_caracteres que reciba un string como argumento.

Dentro de la función, usa len para determinar la longitud de la cadena.

Haz que la función imprima la cadena original y su longitud en el siguiente formato: La frase 'Aprender Python es divertido' tiene 28 caracteres.

Llama a esta función con una frase de tu elección.

Función para convertir y mostrar tipos de números:

Crea una función convertir_numero que tome un número entero como argumento.

Dentro de la función, convierte el número a cadena usando str y a flotante usando float.

Imprime el número en sus tres formas (entero, cadena y flotante) junto con su tipo de dato (usando type) en el siguiente formato:

Entero: 42, Tipo: <class 'int'>
Cadena: 42, Tipo: <class 'str'>
Flotante: 42.0, Tipo: <class 'float'>
Llama a esta función con un número entero de tu elección.



Resultado esperado
La frase 'Aprender Python es divertido' tiene 28 caracteres.

Entero: 42, Tipo: <class 'int'>

Cadena: 42, Tipo: <class 'str'>

Flotante: 42.0, Tipo: <class 'float'> """
# Función para contar caracteres en una cadena
def contar_caracteres(frase):
    longitud = len(frase)
    print(f"La frase '{frase}' tiene {longitud} caracteres.")

# Llamada a la función
contar_caracteres("Aprender Python es divertido")


# Función para convertir y mostrar tipos de números
def convertir_numero(numero):
    numero_cadena = str(numero)
    numero_flotante = float(numero)

    print(f"Entero: {numero}, Tipo: {type(numero)}")
    print()
    print(f"Cadena: {numero_cadena}, Tipo: {type(numero_cadena)}")
    print()
    print(f"Flotante: {numero_flotante}, Tipo: {type(numero_flotante)}")

# Llamada a la función
convertir_numero(42)