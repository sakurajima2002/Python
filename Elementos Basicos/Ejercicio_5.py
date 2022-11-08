#Una tienda ofrece un descuento del 15% sobre el total
#de la compra y un cliente desea saber cuanto debera pagar
#finalmente por su compra.

compra = float(input("Digite el valor de su compra: "))

descuento = compra * 0.15

compra -= descuento

print(f"Total a pagar: {compra:.2f}")