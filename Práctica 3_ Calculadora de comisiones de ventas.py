articulos = {
    1: 239.99,
    2: 129.75,
    3: 99.95,
    4: 350.89
}

salario_base = 200
tasa_comision = 0.09

ventas_totales = 0

print("Calculadora de comisiones de ventas")
print("Ingrese el código del artículo y la cantidad vendida. Para terminar, ingrese 0 como código.")

while True:
    try:
        codigo = int(input("Código del artículo (1-4, 0 para salir): "))
        if codigo == 0:
            break
        if codigo not in articulos:
            print("Código inválido. Intente nuevamente.")
            continue
        cantidad = int(input("Cantidad vendida de este artículo: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Intente nuevamente.")
            continue
        ventas_totales += articulos[codigo] * cantidad
    except ValueError:
        print("Entrada no válida. Intente nuevamente.")

comision = ventas_totales * tasa_comision
salario_del_vendedor = salario_base + comision

print(f"\nEl salario de vendedor es: ${salario_del_vendedor:.2f}")