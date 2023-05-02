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


