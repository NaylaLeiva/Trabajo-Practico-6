#--- ZONA DE VARIABLES ---#
edad_ninio = int()
nombre_ninio = str()
ninio_registrado = int()

#--- ZONA DE FUNCIONES ---#
def menu():
    print("\n--------------------------------------------------")
    print("1) Ingresar datos del niño")
    print("2) Dispositivo mas utilizado")
    print("3) Calcular promedio del tiempo en pantalla (mins)")
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
            dispositivo_mas_utilizado = str(input("Ingrese los dispositivos que más utiliza el niño: tablet, celular o pc: "))
            if (dispositivo_mas_utilizado == "tablet"):
                print("El dispositivo más utilizado es la tablet.")
            elif (dispositivo_mas_utilizado == "celular"):
                print("El dispositivo más utilizado es el celular.")
            elif (dispositivo_mas_utilizado == "pc"):
                print("El dispositivo más utilizado es la PC.")
            else: 
                print("Opción inválida, elija otra vez.")
                opcion = menu() 
        elif (opcion == 3):
            if (dispositivo_mas_utilizado == "tablet"):
                fines_de_uso = str(input("Para que fin usa más la tablet? (juegos, videos, estudios): "))
                if (fines_de_uso == "juegos"):
                    uso_tablet = str(input("Que tan amenudo juega el niño en la tablet? (ocasionalmente, frecuentemente): "))
                    if (uso_tablet == "ocasionalmente"):
                        uso_tablet = 50
                    elif (uso_tablet == "frecuentemente"):
                        uso_tablet = 120
                elif (fines_de_uso == "videos"):
                    uso_tablet = str(input("Que tan amenudo ve videos el niño en la tablet? (ocasionalmente, frecuentemente): "))
                    if (uso_tablet == "ocasionalmente"):
                        uso_tablet = 60
                    elif (uso_tablet == "frecuentemente"):
                        uso_tablet = 180
                elif (fines_de_uso == "estudios"):
                    uso_tablet = str(input("Que tan amenudo estudia el niño en la tablet? (ocasionalmente, frecuentemente): "))
                    if (uso_tablet == "ocasionalmente"):
                        uso_tablet = 30
                    elif (uso_tablet == "frecuentemente"):
                        uso_tablet = 90


            uso_dispositivo = uso_tablet    
            print("elegiste: ",opcion)
        elif (opcion == 4):
            print("elegiste: ",opcion)
        else:
            print("Opcion Invalida, elija otra vez.")
            opcion = menu()
        opcion = menu()
        
    if (ninio_registrado == 1):
        print(f"\nEl niño {nombre_ninio} tiene {edad_ninio} años.")

        print(f"El niño ocupa un total de {uso_dispositivo} minutos al día.")
    
main()
