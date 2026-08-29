print ("===========")
print ("sistema de venta de pizzería")
print ("===========")
nombre_cliente = input("ingrese el nombre del cliente: ")   
variedad_pizza = input("ingrese la variedad de pizza: ")
cantidad_pizzas = int(input("ingrese la cantidad de pizzas: "))
precio_pizza = float(input("ingrese el precio de la pizza: "))

#descuento por comprar>=3 :
#forma de pago
pago = input("ingrese la forma de pago (efectivo/tranferencia): ")
descuento = 0
recargo = 0
if pago == ("efectivo"):
 descuento = subtotal * 0.10
 print("descuento por pago en efectivo: ", descuento)
elif pago == ("transferencia"):
  recargo =0
  print("pago por tranferencia realizado")
else:
    print("forma de pago no valida")
#calcular subtotal
subtotal = cantidad_pizzas * precio_pizza

#acumular datos
total = subtotal - descuento + recargo
cantidad_clientes = cantidad_clientes + 1
total_pizzas = total_pizzas + cantidad_pizzas

print("cliente :", nombre_cliente)
print("variedad de pizza :", variedad_pizza)
print("cantidad de pizzas :", cantidad_pizzas)
print("descuento :", descuento)
print("recargo :", recargo)
print("total a pagar :", total)

#resumen final
print("===========")
print("resumen final")
print("===========")
print("total de clientes atendidos :", cantidad_clientes)
print("total de pizzas vendidas :", total_pizzas)
print("total de ventas :", total_ventas)
print("promedio de ventas por cliente :", total_ventas / cantidad_clientes)

print("============")
print("FIN DEL PROGRAMA")
print("============")



      


 



