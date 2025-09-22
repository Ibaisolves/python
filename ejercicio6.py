print("Introduce una edad")
edad = int(input())
if edad < 0 or edad > 120:
    print("Edad no valida")
#else:
 #   if ()
elif edad < 18:
    print("El alumno es menor de edad")
else:
    print("El alumno es mayor de edad")