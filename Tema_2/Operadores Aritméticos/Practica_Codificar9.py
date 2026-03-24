""" Escribe un programa en Python que contenga una función llamada calcular_calorias. Esta función debe tomar tres argumentos: carbohidratos (cantidad en gramos), proteínas (cantidad en gramos) y grasas (cantidad en gramos). Dentro de la función, utiliza operadores aritméticos para calcular las calorías totales, considerando que cada gramo de carbohidratos y proteínas aporta 4 calorías y cada gramo de grasas aporta 9 calorías. La función debe devolver el total de calorías calculado. Después de definir la función, realiza llamadas a calcular_calorias con diferentes cantidades de macronutrientes y muestra los resultados. Como ejemplo se propone calcular las calorias de una comida con 10 gr de carbohidratos, 40 gr de proteínas y 5 gr de grasa. Resultado esperado Calorías totales: 245"""
def calcular_calorias(carbohidratos, proteinas, grasas):
    # Cada gramo de carbohidratos y proteínas aporta 4 kcal
    # Cada gramo de grasas aporta 9 kcal
    calorias = (carbohidratos * 4) + (proteinas * 4) + (grasas * 9)
    return calorias

# Ejemplo propuesto
resultado = calcular_calorias(10, 40, 5)
print("Calorías totales:", resultado)

# Otras pruebas
print("Calorías totales:", calcular_calorias(50, 20, 10))
print("Calorías totales:", calcular_calorias(30, 30, 15))