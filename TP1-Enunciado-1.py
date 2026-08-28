#--- ZONA DE VARIABLES ---#
edad_ninio = int()
nombre_ninio = str()
ninio_registrado = int()
minutos_por_uso = {
    "tablet": {
        "juegos":   {"ocasionalmente": 50,  "frecuentemente": 120, "nunca": 0},
        "videos":   {"ocasionalmente": 60,  "frecuentemente": 180, "nunca": 0},
        "estudios": {"ocasionalmente": 30,  "frecuentemente": 90, "nunca": 0}
    },
    "pc": {
        "juegos":   {"ocasionalmente": 40, "frecuentemente": 100, "nunca": 0},
        "videos":   {"ocasionalmente": 50, "frecuentemente": 150, "nunca": 0},
        "estudios": {"ocasionalmente": 50, "frecuentemente": 100, "nunca": 0}
    },
    "celular": {
        "juegos":   {"ocasionalmente": 60, "frecuentemente": 120, "nunca": 0},
        "videos":   {"ocasionalmente": 60, "frecuentemente": 120, "nunca": 0},
        "estudios": {"ocasionalmente": 30, "frecuentemente": 70, "nunca": 0}
    }
}
exposicion = {
    "tablet": {}
}

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
            if (edad_ninio >= 3 and edad_ninio <= 12):
                print(f"El niño solo tiene un máximo de 120 minutos de uso de pantalla al día")
            elif (edad_ninio >= 13 and edad_ninio <= 18):
                print(f"El niño solo tiene un máximo de 300 minutos de uso de pantalla al día")
            nombre_ninio = str(input("Ingrese el nombre del niño: "))
            ninio_registrado += 1
        elif (opcion == 2):
            dispositivo_mas_utilizado = str(input("Ingrese los dispositivos que más utiliza el niño: tablet, celular o pc: "))        
            if (dispositivo_mas_utilizado != "tablet" and "celular" and "pc"):
                print("Opción inválida, elija otra vez.")
                opcion = menu() 
        elif (opcion == 3):
            if (dispositivo_mas_utilizado == ""):
                print("Opción inválida, elija la opcion 2 primero.")
                opcion = menu()

            inf = input("Para que fin usa más el dispositivo? (juegos, videos, estudios): ")
            frecuencia = input("Que tan amenudo usa el dispositivo? (ocasionalmente, frecuentemente, nunca): ")
            uso_dispositivo = minutos_por_uso[dispositivo_mas_utilizado][inf][frecuencia]
            print (f"Tiempo estimado de uso del dispositivo {dispositivo_mas_utilizado} para {inf} es de {uso_dispositivo} minutos al día.")
   
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
