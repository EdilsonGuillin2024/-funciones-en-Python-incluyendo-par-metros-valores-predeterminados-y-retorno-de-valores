def calcular_descuento(monto, descuento=10):
    
    monto_descuento = monto * (descuento / 100)
    monto_final = monto - monto_descuento
    return monto_final, monto_descuento

# Solicitamos al usuario que ingrese el monto total de la compra y el porcentaje de descuento
monto_total_compra = float(input("Ingrese el monto total de la compra: "))
descuento_personalizado = float(input("Ingrese el porcentaje de descuento a aplicar (10% por defecto): ") or "10")

# Llamamos a la función con los valores ingresados por el usuario
monto_final, descuento_aplicado = calcular_descuento(monto_total_compra, descuento_personalizado)

# Mostramos el monto original, el descuento aplicado y el monto final a pagar
print(f"Monto original de la compra: {monto_total_compra}")
print(f"Con un descuento del {descuento_personalizado}%, el monto del descuento aplicado es: {descuento_aplicado}")
print(f"El monto final a pagar después del descuento es: {monto_final}")