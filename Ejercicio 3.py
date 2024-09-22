unidad_origen = str(input("Ingrese unidad origen: ")).lower()
temp_unidad_origen = float(input("Ingrese temperatura: "))
unidad_deseada = str(input("Ingrese unidad deseada: ")).lower()
conversion = 0
if unidad_origen == "celcius":
    if unidad_deseada == "fahrenheit":
        conversion= ( 9/5 * temp_unidad_origen ) + 32
        print(conversion)
    elif unidad_deseada == "kelvin":
        conversion = temp_unidad_origen + 273
        print(conversion)
elif unidad_origen == "fahrenheit":
    if unidad_deseada == "celcius":
        conversion= 5/9 * (temp_unidad_origen - 32)
        print(conversion)
    elif unidad_deseada == "kelvin":
        conversion = 5/9 * (temp_unidad_origen - 32) + 273
        print(conversion)
elif unidad_origen == "kelvin":
    if unidad_deseada == "celcius":
        conversion= temp_unidad_origen - 273
        print(conversion)
    elif unidad_deseada == "fahrenheit":
        conversion= 9/5 *(temp_unidad_origen - 32) + 32
        print(conversion)