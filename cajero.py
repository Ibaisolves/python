saldo = 500
while saldo > 0:
    print("Bienvenido al cajero automatico")
    if saldo >= 100:
        print("Su saldo es:", saldo)
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print("Retiro exitoso. Su nuevo saldo es:", saldo)
        else:
            print("Gracias por usar el cajero automatico.")
    if saldo < 100:
        print("Su saldo es inferior a 100. No se puede realizar un retiro.")
    else:
        print("Gracias por usar el cajero automatico.")
