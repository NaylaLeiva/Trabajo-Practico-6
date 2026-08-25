#--- ZONA DE VARIABLES ---#
edad_ninio = int()
nombre_ninio = str()
ninio_registrado = int()

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

#--- ZONA DE CONSOLA ---#
def main():
    ninio_registrado = 0
    opcion = menu()
    
    while (opcion != 5):   
        if (opcion == 1):
            edad_ninio = int(input("Ingrese la edad del niño: "))
            nombre_ninio = str(input("Ingrese el nombre del niño: "))
            ninio_registrado += 1
        elif (opcion == 2):
            print("elegiste: ",opcion)
        elif (opcion == 3):
            print("elegiste: ",opcion)
        elif (opcion == 4):
            print("elegiste: ",opcion)
        else:
            print("Opcion Invalida, elija otra vez.")
            opcion = menu()
        opcion = menu()
        
    if (ninio_registrado == 1):
        print(f"\nEl niño {nombre_ninio} tiene {edad_ninio} años.")
    
main()
