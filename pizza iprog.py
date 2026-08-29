print("=====SISTEMA DE VENTAS DE LA PIZZERIA====")

nombre_cliente = input("Nombre del cliente: ")
variedad_pizza = input("Variedad de pizza: ")
cantidad_pizzas = int(input("Cantidad de pizzas: "))
precio_unitario = float(input("Precio unitario: "))
medio_pago = input("Medio de pago: ")
#calcular el total a pagar
total = cantidad_pizzas * precio_unitario
print(f"total a pagar: ${total}")