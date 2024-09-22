precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
total = 0
descuento = 0
total_desc = 0

if cantidad >= 1 and cantidad <= 4:
    total = precio * cantidad
    if total >= 1000:
        descuento = total * 0.05
        total_desc = total - descuento
        mensaje = f"El total es: {total} \nEl descuento es: {descuento} \nTotal a pagar: {total_desc}"
        print(mensaje)
    elif total < 1000:
        print("No tiene descuneto, su valor a pagar es: ",total)
elif cantidad >= 5 and cantidad <= 9:
    total = precio * cantidad
    if total >= 1000:
        descuento = total * 0.15
        total_desc = total - descuento
    elif total < 1000:
        descuento = total * 0.1
        total_desc = total - descuento
        mensaje = f"El total es: {total} \nEl descuento es: {descuento} \nTotal a pagar: {total_desc}"
        print(mensaje)
elif cantidad >=10 and cantidad <= 19:
    total = precio * cantidad
    if total >= 1000:
        descuento = total * 0.2
        total_desc = total - descuento
    elif total < 1000:
        descuento = total * 0.15
        total_desc = total - descuento
        mensaje = f"El total es: {total} \nEl descuento es: {descuento} \nTotal a pagar: {total_desc}"
        print(mensaje)
elif cantidad >=20:
    total = precio * cantidad
    if total >= 1000:
        descuento = total * 0.25
        total_desc = total - descuento
        mensaje = f"El total es: {total} \nEl descuento es: {descuento} \nTotal a pagar: {total_desc}"
        print(mensaje)
    elif total < 1000:
        descuento = total * 0.20
        total_desc = total - descuento
        mensaje = f"El total es: {total} \nEl descuento es: {descuento} \nTotal a pagar: {total_desc}"
        print(mensaje)


