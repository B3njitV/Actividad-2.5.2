# Inicialización de variable sw
sw = 1

# Menú principal
while sw == 1:
    print("\nMenú Principal:")
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Acción para ver el saldo
            print("Tiene un saldo de $500000")
            confirmacion = input("Presione 1 para volver atrás o 2 para salir: ")
            if confirmacion == "2":
                print("Cierre de sesión exitoso, adiós")
                break
        elif opcion == 2:
            # Acción para retirar dinero
            print("Transferencia realizada")
            confirmacion = input("Presione 1 para volver atrás o 2 para salir: ")
            if confirmacion == "2":
                print("Cierre de sesión exitoso, adiós")
                break
        elif opcion == 3:
            # Salir del programa
            print("Cierre de sesión exitoso, adiós")
            sw = 0
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
    except ValueError:
        print("Error: Ingrese un número válido para la opción.")

