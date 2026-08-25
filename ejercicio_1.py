import math
import time

def menu():
    print("--------------------------------------------------")
    print("1) Ingresar datos del niño")
    print("2) Calcular promedio del tiempo en pantalla (mins)")
    print("3) Dispositivo mas utilizado")
    print("4) Exposicion")
    print("5) Salir")
    print("--------------------------------------------------")
    eleccion = int(input("Elija una opcion! --> "))

    while not (1 <= eleccion <= 5):
        eleccion = int(input("Opcion invalida, intenta otra vez: "))
    
    return eleccion

def main():
    opcion = menu()
    print("Elegiste la opcion: ", opcion)

main()