#función menu
def menu ():
    print("Bievenidos a la calculadora de area de figuras gemoetricas")
    print("1. Calcular area del cuadrado")
    print("2. Calcular area del circulo")
    print("3. Calcular area del triangulo")
    print("4. Calcular area del rectangulo")
    print("5. Calcular area del trapecio")
    print("6. Calcular area del pentagono")
    print("7. Calcular area del hexagono")
    print("8. Calcular area del area sector circular")
    print("9. Salir")
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


def datos_rectangulo ():
    """
    Recibe la base y la altura del rectangulo
    """
    base = float(input("Digite la base del rectangulo: "))
    altura = float(input("Digite la altura del rectangulo: "))
    return base,altura

def datos_trapecio ():
    """
    Recibe la base mayor y menor con la altura del trapecio
    """
    base_mayor = float(input("Digite la base mayor del trapecio: "))
    base_menor = float(input("Digite la base menor del trapecio: "))
    altura = float(input("Digite la altura del trapecio: "))
    return base_mayor,base_menor,altura
def datos_pentagono ():
    """
    Recibe el lado del pentagono
    """
    lado = float(input("Digite el lado del pentagono: "))
  
    return lado
def datos_hexagono():
    """
    Recibe el lado del hexagono
    """
    lado = float(input("Digite el lado del hexagono: "))
  
    return lado

def datos_area_circular():
    """
    Recibe el radio y el angulo del area circular
    """
    radio = float(input("Digite el radio del area circular: "))
    angulo = float(input("Digite el angulo del area circular: "))
    return radio,angulo


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

def mostrar_rectangulo(area):
    """
    muestra el area del rectangulo al usuario final
    """
    print(f"El area del rectangulo es {area} ,mts^2")

def mostrar_trapecio(area):
    """
    muestra el area del trapecio al usuario final
    """
    print(f"El area del trapecio es {area} ,mts^2")

def mostrar_pentagono(area):
    """
    muestra el area del pentagono al usuario final
    """
    print(f"El area del pentagono es {area} ,mts^2")

def mostrar_hexagono(area):
    """
    muestra el area del hexagono al usuario final
    """
    print(f"El area del hexagono es {area} ,mts^2")

def mostrar_area_circular(area):
    """
    muestra el area del area_circular al usuario final
    """
    print(f"El area del area_circular es {area} ,mts^2")