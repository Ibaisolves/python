print("Muestrame una nota")
nota = int(input())
if nota < 0 or nota > 10:
    print("Nota no valida")
elif nota < 5: 
    print("Insuficiente")
elif nota < 5 or nota < 6:
    print("Suficiente")
elif nota < 6 or nota < 7:
    print("Bien")
elif nota < 7 or nota < 9:
    print("Notable")
else:
    print("Sobresaliente")  
if nota < 0 or nota > 10:
    print("Nota no valida")
    
