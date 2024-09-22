nota = float(input("Ingrese su nota del 0 al 100: "))

if nota < 0 and nota > 100:
    print("Error, nota invalida")
elif nota >= 0 and nota <= 59:
    print("f")
elif nota >= 60 and nota <= 69:
    print("D")
elif nota >= 70 and nota <= 79:
    print("C")
elif nota >= 80 and nota <= 89:
    print("B")
elif nota >= 90:
    print("A")
