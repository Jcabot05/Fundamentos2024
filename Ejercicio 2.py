estado_civil = str(input("Ingrese el estado civil: ")).lower()
sueldo_anual = float(input("Ingrese el sueldo anual: "))
impuesto = 0
if estado_civil == "soltero":
    if sueldo_anual < 30000:
        impuesto = sueldo_anual * 0.10
        print("Su impuesto es: ", impuesto)
    elif sueldo_anual >= 30000 and sueldo_anual <= 70000:
        impuesto = sueldo_anual * 0.20
        print("Su impuesto es: ", impuesto)
    elif sueldo_anual >= 70000:
        impuesto = sueldo_anual * 0.30
        print("Su impuesto es: ", impuesto)
elif estado_civil == "casado":
    if sueldo_anual <= 40000:
        impuesto = sueldo_anual * 0.08
        print("Su impuesto es: ", impuesto)
    elif sueldo_anual > 40000 and sueldo_anual <= 90000:
        impuesto = sueldo_anual * 0.15
        print("Su impuesto es: ", impuesto)
    elif sueldo_anual > 90000:
        impuesto = sueldo_anual * 0.25
        print("Su impuesto es: ", impuesto)