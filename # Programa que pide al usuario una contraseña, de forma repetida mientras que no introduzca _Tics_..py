# Cuando finalmente escriba la contraseña correcta, se le dira "Bienvenido" y termina el programa.
secreto = "Tics"
clave = input("Dime la clave:")
while clave != secreto:
    print("Clave incorrecta!!!")
    clave = input("Dime la clave:")
    print("Bienvenido!!!")
    print("Programa terminado")