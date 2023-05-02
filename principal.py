from operaciones import *
from interfaz import *
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
RECTANGULO = 4
TRAPECIO = 5
PENTAGONO = 6
HEXAGONO = 7
SECTOR_CIRCULAR= 8
SALIR = 9
#
opcion = 0

while opcion != SALIR:
    opcion = menu()

    if opcion ==CUADRADO:
        #llamar la funcion de solicitar datos
        lado = datos_cuadrado()
        #llamar a area
        area = area_cuadrado(lado)
        #Llamar a mostrar datos
        mostrar_cuadrado(area)
    elif opcion ==CIRCULO:
        #llamar la funcion de solicitar datos
        radio = datos_circulo()
        #llamar a area
        area = area_circulo(radio)
        #Llamar a mostrar datos
        mostrar_circulo(area)
    elif opcion ==TRIANGULO:
        #llamar la funcion de solicitar datos
        base,altura = datos_triangulo()
        #llamar a area
        area = area_triangulo(base,altura)
        #Llamar a mostrar datos
        mostrar_triangulo(area)
    elif opcion ==RECTANGULO:
        #llamar la funcion de solicitar datos
        base,altura = datos_rectangulo()
        #llamar a area
        area = area_rectangulo(base,altura)
        #Llamar a mostrar datos
        mostrar_rectangulo(area)
    elif opcion ==TRAPECIO:
        #llamar la funcion de solicitar datos
        base_mayor,base_menor,altura = datos_trapecio()
        #llamar a area
        area = area_trapecio(base_mayor,base_menor,altura)
        #Llamar a mostrar datos
        mostrar_trapecio(area)
    elif opcion ==PENTAGONO:
        #llamar la funcion de solicitar datos
        lado= datos_pentagono()
        #llamar a area
        area = area_pentagono(lado)
        #Llamar a mostrar datos
        mostrar_pentagono(area)
    elif opcion ==HEXAGONO:
        #llamar la funcion de solicitar datos
        lado= datos_hexagono()
        #llamar a area
        area = area_hexagono(lado)
        #Llamar a mostrar datos
        mostrar_hexagono(area)
    elif opcion ==SECTOR_CIRCULAR:
        #llamar la funcion de solicitar datos
        radio,angulo= datos_area_circular()
        #llamar a area
        area = area_sector_circular(radio,angulo)
        #Llamar a mostrar datos
        mostrar_area_circular(area)
    elif opcion == SALIR:
        break 
    else:
        print("ERROR!!!!!")
print("gracias por usar nuestro programa")