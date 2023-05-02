from operaciones import area_cuadrado,area_circulo,area_triangulo
from interfaz import menu,datos_cuadrado,datos_circulo,datos_triangulo,mostrar_circulo,mostrar_cuadrado,mostrar_triangulo

CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
SALIR = 4
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
    elif opcion == SALIR:
        break 
    else:
        print("ERROR!!!!!")
print("gracias por usar nuestro programa")