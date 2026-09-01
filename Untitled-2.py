#inicialización de contadores
cantidad_clientes = 0
total_pizzas = 0
print ("===========")
print ("sistema de venta de pizzería")
print ("===========")
nombre_cliente = input("ingrese el nombre del cliente: ")   
variedad_pizza = input("ingrese la variedad de pizza: ")
cantidad_pizzas = int(input("ingrese la cantidad de pizzas: "))
precio_pizza = float(input("ingrese el precio de la pizza: "))

#calcular subtotal
subtotal = cantidad_pizzas * precio_pizza
#forma de pago
pago = input("ingrese la forma de pago (efectivo/transferencia): ")
descuento = 0
recargo= 0
# evaluamos el pago y aplicamos descuento o recargo
if pago == "efectivo":
    descuento = subtotal * 0.10
    print("descuento por pago en efectivo: ", descuento)
elif pago == "transferencia":
    recargo = subtotal * 0.05
    print("pago por transferencia realizado")
else:
    print("forma de pago no válida")
#acumular datos
total= subtotal - descuento + recargo
cantidad_clientes = cantidad_clientes + 1
total_pizzas = total_pizzas + cantidad_pizzas
total_ventas = total_ventas + total
print(f"""
cliente: {nombre_cliente}
variedad de pizza: {variedad_pizza}
cantidad de pizzas: {cantidad_pizzas}
descuento: {descuento}
recargo: {recargo}
total a pagar: {total}
""")

#resumen final
print(f"""
total de clientes atendidos: {cantidad_clientes}
total de pizzas vendidas: {total_pizzas}  
total de ventas: {total_ventas: .2f}
""")

print("============")
print("FIN DEL PROGRAMA")
print("============")