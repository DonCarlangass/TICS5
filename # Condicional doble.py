# Condicional doble
print ('Programa que devuelve si eres mayor o menor de edad')
# Pedimos que el usuario ingrese su edad y la convertimos entero
edad = int(input('Escribe tu edad en años:\n'))
# Realizamos la condicional simple
if edad >= 18:
    #Imprimimos la instruccion cuando la condicion es verdadero
    print('Eres mayor de edad')
    # Si no se cumple la condicion
else:
    # imprimimos la instruccion cuando la condicion es falsa
    print('Eres menor de edad')