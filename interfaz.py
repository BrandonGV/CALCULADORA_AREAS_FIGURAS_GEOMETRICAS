#función menu
def menu ():
    print("Bievenidos a la calculadora de area de figuras gemoetricas")
    print("1. Calcular area del cuadrado")
    print("2. Calcular area del circulo")
    print("3. Calcular area del triangulo")
    print("4. Salir")
    op =int (input("Digite su opción: "))
    return op
#función solicitar datos
def datos_cuadrado ():
    """
    Recibe el lado del cuadrado
    """
    lado = float(input("Digite el lado del cuadrado: "))
    return lado    

def datos_circulo ():
    """
    Recibe el radio del circulo
    """
    radio = 2
    return radio 

def datos_triangulo ():
    """
    Recibe la base y la altura del triangulo 
    """
    base = float(input("Digite la base del triangulo: "))
    altura = float(input("Digite la altura del triangulo: "))
    return base,altura

#funcio mostrar datos
def mostrar_cuadrado(area):
    """
    muestra el area del cuadrado al usuario final
    """
    print(f"El area del cuadrado es {area} ,mts^2")

def mostrar_circulo(area):
    """
    muestra el area del circulo al usuario final
    """
    print(f"El area del circulo es {area} ,mts^2")

def mostrar_triangulo(area):
    """
    muestra el area del triangulo al usuario final
    """
    print(f"El area del triangulo es {area} ,mts^2")

