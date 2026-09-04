#--- ZONA DE VARIABLES ---#
edad_ninio = int()
nombre_ninio = str()

#--- ZONA DE FUNCIONES ---#
def menu():
    print("\n--------------------------------------------------")
    print("1) Ingresar datos del niño")
    print("2) Calcular promedio del tiempo en pantalla (mins)")
    print("3) Dispositivo mas utilizado")
    print("4) Exposicion")
    print("5) Salir")
    print("--------------------------------------------------")
    eleccion = int(input("\nElija una opcion! --> "))
    return eleccion

def promedio():
    again = True
    resultado = 0
    cantidad = 0
    dispositivos = {
        1: ["celular", 0],
        2: ["pc", 0],
        3: ["laptop", 0],
        4: ["tablet", 0]
    }
    
    while (again):
        print("\n1) celular")
        print("2) pc")
        print("3) laptop")
        print("4) tablet")
        eleccion = int(input("Elija el dispositivo: "))
        
        if (eleccion < 1 or eleccion > 4):
            print("\nDispositivo inválido.")
            continue
            
        if (dispositivos[eleccion][1] != 0):
            print("\nEse dispositivo ya fue ingresado.")
        else:
            tiempo = int(input("\nCuanto tiempo lo usa? (mins) "))
            dispositivos[eleccion][1] = tiempo
            resultado += tiempo
            cantidad += 1
            
            print("\nDesea añadir otro dispositivo?")
            print("1) Si / 2) No")
            respuesta = int(input())
            if (respuesta == 2):
                again = False
    
    if (cantidad != 0):           
        resultado = resultado / cantidad
    
    return resultado, dispositivos

def mostrar_dispositivos(dispositivos):
    mayor = dispositivos[1][1]
    nombre_mayor = dispositivos[1][0]

    for x in dispositivos:
        if dispositivos[x][1] > mayor:
            mayor = dispositivos[x][1]
            nombre_mayor = dispositivos[x][0]

    print("\nDispositivo más usado:", nombre_mayor,"- Con:", mayor, " mins registrados.")
    
    return mayor

def expocicion(dispositivos, edad_ninio):
    expocicion_total = dispositivos[1][1] + dispositivos[2][1] + dispositivos[3][1] + dispositivos[4][1]
    
    if (edad_ninio < 4):
        print("su ninio no deberia usar disositivos aun, se le recomienda un maximo de 20 mins.")
    elif (4 <= edad_ninio < 12):
        if(expocicion_total >= 120):
            print("Su niño tiene una expocicion mayor al promedio para su edad, se recominada reducir el tiempo en pantall.")
        else:
            print("Su niño tiene un uso adecuado para el tiempo en pantalla")
    elif (12 <= edad_ninio < 18):
        if(expocicion_total >= 320):
            print("Su niño tiene una expocicion mayor al promedio para su edad, se recominada reducir el tiempo en pantall.")
        else:
            print("Su niño tiene un uso adecuado para el tiempo en pantalla")
    else:
        print("Su niño es un adulto, promedio general recomendado es de 8 horas (480 mins)")
    
    print("Exposicion del ninio: ", expocicion_total, "(tiempo total de minutos en pantallas)")
        
    return expocicion_total
    
#--- ZONA DE CONSOLA ---#
def main():
    opcion = menu()
    registro = 0
    ninioreg = 0
    while (opcion != 5):   
        if (opcion == 1):
            edad_ninio = int(input("\nIngrese la edad del niño: "))
            nombre_ninio = str(input("Ingrese el nombre del niño: "))
            ninioreg += 1
            if (ninioreg != 0):
                    print(f"\nEl niño {nombre_ninio} tiene {edad_ninio} años.")
            registro = 1
        elif (opcion == 2):
            if(registro >= 1):
                promedio_Dis, dispositivos = promedio()
                print("\nEl promedio es: ", promedio_Dis)
                registro = 2
            else:
                print("Completa la opcion anterior primero")
        elif (opcion == 3):
            if(registro >= 2):
                mostrar_dispositivos(dispositivos)
                registro = 3
            else:
                print("Completa la opcion anterior primero")
        elif (opcion == 4):
            if(registro >= 3):
                expocicion_total = expocicion(dispositivos, edad_ninio)
            else:
                print("Completa la opcion anterior primero")
        else:
            print("Opcion Invalida, elija otra vez.")
            opcion = menu()
        opcion = menu()
        
    print(nombre_ninio, "tiene", edad_ninio, "años de edad y tiene una expocicion de:", expocicion_total , "\n")
    
main()