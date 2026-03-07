"""Instrucciones

Escribe un programa en Python que incluya una función personalizada para generar la distancia a un planeta.

La función debe recibir como argumento un string que proporcionará el nombre del planeta y un número entero que será la distancia en millones de km a dicho planeta.

Tras definir la función, esta imprimirá por pantalla el nombre del planeta y la distancia al mismo.



Resultado esperado

Nombre del planeta: Marte

Distancia al planeta: 225 millones de km



"""

def distancia_planeta(arg1, arg2):

    print(f"Nombre del planeta: {arg1} Distancia al planeta: {arg2} millones de km")

# Llamada a la función
distancia_planeta("Marte", 225)
distancia_planeta("Jupiter", 778)
distancia_planeta("Venus", 50)