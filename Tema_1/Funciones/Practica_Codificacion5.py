"""
Instrucciones

Escribe un programa en Python que analice la longitud de los títulos de varios libros utilizando la función len().

El programa tendrá predefinidos varios títulos de libros como strings.

Usa la función len() para calcular la longitud de cada título (número de caracteres, incluyendo espacios).

Después de calcular la longitud de cada título, usa print para mostrar el título del libro y su respectiva longitud. Recuerda que puedes hacer uso del concepto de f-string que exploramos en ejercicios anteriores.



Resultado esperado

La longitud del título del libro 1 es: 20

La longitud del título del libro 2 es: 23

La longitud del título del libro 3 es: 24 


"""

#Títulos de los libros
titulo1 = "Cien años de soledad"
titulo2 = "El señor de los anillos"
titulo3 = "Don Quijote de la Mancha"

len1 = len(titulo1)
len2 = len(titulo2)
len3 = len(titulo3)

print(f"Titulo: {titulo1} tamaño: {len1}" )
print(f"Titulo: {titulo2} tamaño: {len2}" )
print(f"Titulo: {titulo3} tamaño: {len3}" )