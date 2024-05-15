puntos = 100000

while True:
    print("Seleccione una opción:")
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")

    op = int(input("Ingrese su opción: "))

    if op == 1:
        print(f"Tienes {puntos} puntos")
    elif op == 2:
        print("Seleccione el producto a canjear:")
        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de: 25.000 puntos")
        print("3.- Disco duro portátil, valor de: 30.000 puntos")
        
        continu = int(input("Seleccione la opción: "))
        if continu == 1:
            if puntos >= 10000:
                puntos -= 10000
                print(f"Canje exitoso, le quedan: {puntos} puntos")
            else:
                print("No tienes suficientes puntos para canjear este producto.")
        elif continu == 2:
            if puntos >= 25000:
                puntos -= 25000
                print(f"Canje exitoso, le quedan: {puntos} puntos")
            else:
                print("No tienes suficientes puntos para canjear este producto.")
        elif continu == 3:
            if puntos >= 30000:
                puntos -= 30000
                print(f"Canje exitoso, le quedan: {puntos} puntos")
            else:
                print("No tienes suficientes puntos para canjear este producto.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
    elif op == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")