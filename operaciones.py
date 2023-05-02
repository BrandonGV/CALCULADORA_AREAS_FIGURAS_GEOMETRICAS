import math

#funciones
def area_cuadrado (lado):
    """
    calcula el area del cuadrado y retorna una varible
    en formato float
    """
    area=lado*lado
    return area

def area_circulo (radio):
    """
    calcula el area del circulo y retorna una varible
    en formato float
    """
    area= math.pi*radio**2
    return area

def area_triangulo (base,altura):
    """
    calcula el area del triangulo y retorna una varible
    en formato float
    """
    area= base*altura/2
    return area

def area_rectangulo(base, altura):
    """
    calcula el area del rectangulo y retorna una variable en formato float
    """
    area = base * altura
    return area

def area_trapecio(base_mayor, base_menor, altura):
    """
    calcula el area del trapecio y retorna una variable en formato float
    """
    area = (base_mayor + base_menor) * altura / 2
    return area

def area_pentagono(lado):
    """
    calcula el area del pentagono regular y retorna una variable en formato float
    """
    apotema = lado / (2 * math.tan(math.pi/5))
    perimetro = 5 * lado
    area = perimetro * apotema / 2
    return area

def area_hexagono(lado):
    """
    calcula el area del hexagono regular y retorna una variable en formato float
    """
    apotema = lado * math.sqrt(3) / 2
    perimetro = 6 * lado
    area = perimetro * apotema / 2
    return area

def area_sector_circular(radio, angulo):
    """
    calcula el area del sector circular y retorna una variable en formato float
    """
    area_circulo = math.pi * radio**2
    area_sector = area_circulo * angulo / (2 * math.pi)
    return area_sector



