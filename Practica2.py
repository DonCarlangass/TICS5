# Imprimir el menú de operaciones aritméticas
print("""
Opciones para elegir:
1: Suma
2: Resta
3: Multiplicación
4: División
""")

# Pedir al usuario que elija una opción del menú
op = int(input('Ingrese el número de la opción deseada:\n'))

# Evaluamos la condición 1
if op == 1:
   
    # Pedir los datos que se necesitan
    num1 = int(input('Escribe el primer número:\n'))
    num2 = int(input('Escribe el segundo número:\n'))
  
    # Realizar la operación
    print(f'La suma es {num1 + num2}')

# Evaluamos la condición 2
elif op == 2:
   
    # Pedir los datos que se necesitan
    num1 = int(input('Escribe el primer número:\n'))
    num2 = int(input('Escribe el segundo número:\n'))
    
    # Realizar la operación
    print(f'La resta es {num1 - num2}')

# Evaluamos la condición 3
elif op == 3:
   
    # Pedir los datos que se necesitan
    num1 = int(input('Escribe el primer número:\n'))
    num2 = int(input('Escribe el segundo número:\n'))
   
    # Realizar la operación
    print(f'La multiplicación es {num1 * num2}')

# Evaluamos la condición 4
elif op == 4:
   
    # Pedir los datos que se necesitan
    num1 = int(input('Escribe el primer número:\n'))
    num2 = int(input('Escribe el segundo número:\n'))
   
    # Verificar división por cero
    if num2 != 0:
        print(f'La división es {num1 / num2}')
    else:
        print('Error: No se puede dividir entre cero')

# Evaluamos si no se cumple ninguna condición
else:
    print('La opción elegida no es válida')