#--- ZONA DE VARIABLES ---#

pizza = {
    1: ["Pizza Mozarella", 2000],
    2: ["Pizza Roquefort", 2500],
    3: ["Pizza 4 quesos", 3000],
    4: ["Pizza Margarita", 2300]
}

#--- ZONA DE FUNCIONES ---#

def menu_eleccion():
    print("\n---------Ordenar Pizzas!--------")
    print("1) Ver menu y seleccionar pedido")
    print("2) Ver mis pedidos seleccionados")
    print("3) Confirmar pago")
    print("4) Cancelar todo y salir")
    pedido = int(input("\nSelecciona una opcion\n"))
    return pedido


def menu_pizzas():
    pedidos = [] #Una lista porque no se me ocurrio otra manera de guardar varios pedidos sin usar muchas variables
    while (True):
        print("\n--------------MENU--------------")
        print("\nOpciones disponibles (Nombre y Precio en pesos):\n")
        print("1)",pizza[1][0],"------- Precio:",pizza[1][1],"$")
        print("2)",pizza[2][0],"------- Precio:",pizza[2][1],"$")
        print("3)",pizza[3][0],"------- Precio:",pizza[3][1],"$")
        print("4)",pizza[4][0],"------- Precio:",pizza[4][1],"$")
        
        eleccion = int(input("\nSelecciona un pedido disponible: "))
        
        pedidos.append(pizza[eleccion])
        
        print("\nDesea añadir otro pedido?")
        print("1) Si / 2) No")
        
        while (True):
            salir = int(input())
            
            if (salir == 1 or salir == 2):
                break
            else:
                print("Opcion invalida, elija otra vez")
        
        if (salir == 2):
            break
        
    return pedidos

def ver_pedidos(seleccion):
    print("\nEstos son sus pedidos actuales seleccionados: ")
    print(seleccion)
    
    pago = 0
    
    for x in seleccion:
        pago += x[1]
        
    print("Pago total:",pago,"$")
    
    return pago

def confirmar_pago(total):
    print("\n----------¡Aviso!----------\n")
    print("1) Pagar en efectivo en el local (Incluira un 5% de descuento al precio total)")
    print("2) Pagar con credito (Incluira un 10% de recargo al precio toal)")
    print("3) Pagar con debito (Incluira un 3% de recargo al precio toal)\n")
    
    metodo_pago = int(input("Seleccione el metodo de pago: "))
    
    while(0 == metodo_pago or metodo_pago > 3):
        print("Opcion invalida, elija un metodo de pago existente")
        metodo_pago = int(input("Seleccione el metodo de pago: "))
        
    precio_calculado = precio_final(metodo_pago, total)
    print("El precio final a pagar sera:", precio_calculado, "$")
    
    return precio_calculado
    
        

def precio_final(metodo_pago, total):
    if(metodo_pago == 1):
        total -= total * 5 / 100
    elif(metodo_pago == 2):
        total += total * 10 / 100
    else:
        total += total * 3 / 100
        
    return total

#--- ZONA DE CONSOLA ---#

def main():
    opcion = menu_eleccion()
    avanzar = 0
    while(opcion != 4):
        if(opcion == 1):
            seleccion = menu_pizzas()
            print("\n", seleccion)
            avanzar = 1
        elif(opcion == 2):
            if(avanzar >= 1):
                total = ver_pedidos(seleccion)
                avanzar = 2
            else:
                print("No tiene pedidos registrados!")
        elif(opcion == 3):
            if(avanzar >=2):
                confirmar_pago(total)
                break
            else:
                print("No tiene Pedidos a pagar")
        else:
            print("opcion invalida")
        opcion = menu_eleccion()
    
    if(avanzar >= 2):
        print("Compra realizada!\n")

main()