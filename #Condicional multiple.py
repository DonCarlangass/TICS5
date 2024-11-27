# Condicional multiple
"""Infancia (0 - 11 años); Adolescencia (12 - 18 años); Juventud (14 - 26 años);
Adultez (27- 59 años); Persona Mayor (60 años o mas)"""
print("Programa que devuelve la etapa del ciclo de la vida segun la edad")
# Pedimos que el usuario ingrese su edad y la convertimos en entero
edad = int(input("Escribe tu edad en años: \n"))
# Realisamos la evaluacion de la condicion 1
if edad <= 11:
    # Imprimimos la instruccion cuando la condicion 1 es verdadera
    print("Infancia")
# Si no cimple la condicion 1, realizamos la condicion 2
elif edad >= 12 and edad < 18:
    # Imprimimos la instruccion cuando la condicion 2 es verdadera
    print("Adolescencia")
# Si no se cumple la condicion 2, realizamos la condicion 3
elif edad >= 19 and edad < 30:
    # Imprimimos la instruccion cuando la condicion 3 es verdadera
    print("Juventud")
# Si no se cumple la condicion 3, realizamos la condicion 4
elif edad >= 30 and edad < 60:
    # Imprimimos la instruccion cuando la condicion 4 es verdadera
    print("Adultez")
# Si no se cumple la condicion 4
else:
    # Ejecutamos la ultima instruccion o bloque de instrucciones
    print("Persona mayor")