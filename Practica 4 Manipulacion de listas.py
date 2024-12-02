PagoVentas = []

def calcular_pago(venta_semanal):
    salario_base = 500
    comision = venta_semanal * 0.12
    pago_total = salario_base + comision
    return salario_base, comision, pago_total

def agregar_vendedor():
    nombre = input("Ingrese el nombre del vendedor: ")
    venta_semanal = float(input("Ingrese la venta semanal del vendedor: "))
    salario_base, comision, pago_total = calcular_pago(venta_semanal)
    PagoVentas.append({
        "nombre": nombre,
        "venta_semanal": venta_semanal,
        "comision": comision,
        "pago_total": pago_total
    })
    print(f"Vendedor {nombre} agregado con éxito.")

def eliminar_vendedor():
    nombre = input("Ingrese el nombre del vendedor a eliminar: ")
    for vendedor in PagoVentas:
        if vendedor["nombre"] == nombre:
            PagoVentas.remove(vendedor)
            print(f"Vendedor {nombre} eliminado con éxito.")
            return
    print("No se encontró un vendedor con ese nombre.")

def mostrar_vendedores():
    if not PagoVentas:
        print("No hay vendedores registrados.")
        return
    for vendedor in PagoVentas:
        print(f"\nNombre: {vendedor['nombre']}")
        print(f"Venta semanal: ${vendedor['venta_semanal']:.2f}")
        print(f"Comisión: ${vendedor['comision']:.2f}")
        print(f"Pago total: ${vendedor['pago_total']:.2f}")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar vendedor")
        print("2. Eliminar vendedor")
        print("3. Mostrar vendedores")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_vendedor()
        elif opcion == "2":
            eliminar_vendedor()
        elif opcion == "3":
            mostrar_vendedores()
        elif opcion == "4":
            print("Saliendo del programa. ¡Adios!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()