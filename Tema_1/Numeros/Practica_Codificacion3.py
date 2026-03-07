""" Crea una variable llamada nombre_astronauta y asígnale tu nombre como un string.

Crea una variable edad_astronauta y asígnale tu edad como un número.

Crea una variable destino y asígnale el nombre de un planeta como string (por ejemplo, "Marte").

Imprime un mensaje de introducción utilizando estas variables, que diga: "Hola, soy [nombre_astronauta], tengo [edad_astronauta] años y mi próximo destino es [destino]."

Crea dos variables, combustible y velocidad, asignándoles valores numéricos.

Imprime un mensaje que diga: "Estoy navegando a [velocidad] km/s con [combustible]% de combustible restante hacia [destino]."

Explora el concepto de f-string para insertar las variables en las cadenas de texto y mostrarlas por pantalla utilizando print.

Al usar f-strings, debes colocar el nombre de la variable entre {} dentro del string. Por ejemplo: print(f"Texto {variable}").



Resultado esperado:

Diario de un Astronauta



Hola, soy Max, tengo 25 años y mi próximo destino es Marte.

Estoy navegando a 27000 km/s con 85% de combustible restante hacia Marte.



Fecha: 2024-01-10

Hoy experimentamos con el cultivo de plantas en microgravedad.

Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!



Fecha: 2024-01-11

Realizamos una caminata espacial para reparar un panel solar.

Mensaje personal: Flotar en el espacio nunca deja de asombrarme.

"""

print("Diario de un Astronauta\n")
 
print("Fecha: 2024-01-10")
print("Hoy experimentamos con el cultivo de plantas en microgravedad.")
print("Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!\n")
 
print("Fecha: 2024-01-11")
print("Realizamos una caminata espacial para reparar un panel solar.")
print("Mensaje personal: Flotar en el espacio nunca deja de asombrarme.\n")

nombre_astronauta = "Samuel"
edad_astronauta = 19
destino = "Marte"

print(f"Hola soy {nombre_astronauta} , tengo  {edad_astronauta}  años y mi proximo destino es  {destino}")

combustible = 45
velocidad = 100

print(f"Estoy navegando a  {velocidad}km/s con  {combustible} % de combustible restante hacia  {destino}")