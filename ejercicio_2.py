#--- ZONA DE VARIABLES ---#
opcion_pizza = {
    "1": {"nombre": "Pizza Napolitana", "precio": 10000},
    "2": {"nombre": "Pizza Muzarrella", "precio": 12000},
    "3": {"nombre": "Pizza Calabresa", "precio": 13000},
    "4": {"nombre": "Pizza Especial", "precio": 15000},
    "5": {"nombre": "Pizza Fugazzeta", "precio": 16000}
} 
pago = {
    "1": {"nombre": "Efectivo", "valor": "descuento", "recarge": 10},
    "2": {"nombre": "Tarjeta de crédito", "valor": "recargo", "recarge": 5},
    "3": {"nombre": "Tarjeta de débito", "valor": "recargo", "recarge": 5}
}

#--- ZONA DE FUNCIONES ---#
print("\n--------------------¡Bienvenido a Pizzeria Iprog!------------------------------")
Cliente= str(input("Ingrese el nombre del cliente: "))
def menu():
    print("\n--------------------------------------------------")
    print("1) Pedir pizza")
    print("2) Cantidad de pizzas pedidas")
    print("3) Continuar con el pago")
    print("4) Cancelar pedido")
    print("--------------------------------------------------")
    eleccion = int(input("\nElija una opcion! --> "))
    return eleccion

def pizza():
    print("\n--------------------------------------------------")
    print("1) Pizza Napolitana")
    print("2) Pizza Muzarrella")
    print("3) Pizza Calabresa")
    print("4) Pizza Especial")
    print("5) Pizza Fugazzeta")
    print("--------------------------------------------------")
    eleccion_pizza = int(input("\nQue pizza desea? --> "))
    return eleccion_pizza

def metodo_pago():
    print("\n--------------------------------------------------")
    print("1) Efectivo, incluye un 5% de descuento")
    print("2) Tarjeta de crédito, incluye un 10% de recargo")
    print("3) Tarjeta de débito, incluye un 5% de recargo")
    print("--------------------------------------------------")
    eleccion = int(input("\nElija su método de pago! --> "))
    return eleccion

def calcular_total(cantidad_pizzas, opcion_pago, id_pizza, total_a_pagar, Cliente):
    print("\n--------------------------------------------------")
    print(f"El cliente {Cliente} ha pedido {cantidad_pizzas} {opcion_pizza[str(id_pizza)]['nombre']}.")
    print(f"El total a pagar es de ${total_a_pagar:.2f} con descuento/recargo incluido.")
    print(f"Metodo de pago elegido: {pago[str(opcion_pago)]['nombre']}.")
    print(f"Se incluye un {pago[str(opcion_pago)]['valor']} del {pago[str(opcion_pago)]['recarge']}%")
    print("--------------------------------------------------")
    eleccion = int(input("\nDesea agregar a otro cliente? (1) o cancelar? (2) --> "))
    return eleccion
          
#--- ZONA DE CONSOLA ---#
def main():
    opcion = menu()
    id_pizza = None
    cantidad_pizzas = 0
    opcion_pago = None
    while (opcion != 4):   
        if (opcion == 1):
            id_pizza = pizza()
            if (id_pizza == 1):
                print(f"Has elegido la {opcion_pizza[str(id_pizza)]['nombre']} con un precio de ${opcion_pizza[str(id_pizza)]['precio']}.")              
                opcion = menu() 
            elif (id_pizza == 2):
                print(f"Has elegido la {opcion_pizza[str(id_pizza)]['nombre']} con un precio de ${opcion_pizza[str(id_pizza)]['precio']}.")
                opcion = menu()
            elif (id_pizza == 3):
                print(f"Has elegido la {opcion_pizza[str(id_pizza)]['nombre']} con un precio de ${opcion_pizza[str(id_pizza)]['precio']}.")
                opcion = menu()      
            elif (id_pizza == 4):
                print(f"Has elegido la {opcion_pizza[str(id_pizza)]['nombre']} con un precio de ${opcion_pizza[str(id_pizza)]['precio']}.")
                opcion = menu()
            elif (id_pizza == 5):
                print(f"Has elegido la {opcion_pizza[str(id_pizza)]['nombre']} con un precio de ${opcion_pizza[str(id_pizza)]['precio']}.")
                opcion = menu()        
            elif (id_pizza != 1 and id_pizza != 2 and id_pizza != 3 and id_pizza != 4 and id_pizza != 5):
                print("Opción inválida, elija otra vez.")
                id_pizza = pizza()      
        elif (opcion == 2):
            cantidad_pizzas = int(input("Ingrese la cantidad de pizzas pedidas (Con descuento del 10% a partir de 3 unidades): "))
            print(f"Ha pedido {cantidad_pizzas} pizzas.")
            opcion = menu()
        elif (opcion == 3):
            if id_pizza is None:
                print("No ha seleccionado ninguna pizza.")
                opcion = menu()
                continue
            elif cantidad_pizzas == 0:
                print("No ha ingresado la cantidad de pizzas.")
                opcion = menu()
                continue
            else:
                nombre_pizza = opcion_pizza[str(id_pizza)]["nombre"]
                precio_pizza = opcion_pizza[str(id_pizza)]["precio"]
                total_a_pagar = cantidad_pizzas * precio_pizza
                descuento = True and cantidad_pizzas >= 3
                if descuento:
                    total_a_pagar *= 0.9  # Aplicar un descuento del 10%
            print(f"El cliente {Cliente} ha pedido {cantidad_pizzas} {nombre_pizza} .")
            print(f"El total a pagar es de ${total_a_pagar:.2f}.")
            print(f"Por favor, elija su método de pago.")
            opcion_pago = metodo_pago()
            if opcion_pago == 1:
                total_a_pagar *= 0.95  # Se aplica un descuento del 5%
            elif opcion_pago == 2:
                total_a_pagar *= 1.10  # Se aplica un recargo del 10%
            elif opcion_pago == 3:
                total_a_pagar *= 1.10  # Se aplica un recargo del 10%
            menu_final = calcular_total(cantidad_pizzas, opcion_pago, id_pizza, total_a_pagar, Cliente)
            if menu_final == 1:
                    print("Se ha agregado otro cliente.")
                    main()  # Se reinicia el proceso para un nuevo cliente
            elif menu_final == 2:
                    print("------------------Pedido cancelado.---------------------")
                    break       
main()