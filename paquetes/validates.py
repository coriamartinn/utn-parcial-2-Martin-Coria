import pygame as pg

def verificar_estado(areas: tuple, posicion_click: tuple) -> str:
    """
    Esta funcion se encarga de verificar el estado del juego, 
    para saber que interfaz de usuario debe ser mostrada en el juego. 
    ESTADOS DISPONIBLES -> "MENU" (DEFAULT) | "JUGAR" | "PUNTAJES" | "SALIR"
    Args:
        posicion_click (tuple): Recibe la tupla con las coordenadas de donde se utilizo el click del mouse por ultima vez
        areas (tuple): recibe los rects
    Returns:
        str: Devuelve el estado verificado
    """
    
    estado = "MENU"
    
    jugar = areas[0]
    puntajes = areas[1]
    salir = areas[2]
    
    if  jugar.collidepoint(posicion_click):
        estado = "JUGAR"
    elif puntajes.collidepoint(posicion_click):
        estado = "PUNTAJES"
    if salir.collidepoint(posicion_click):
        estado = "SALIR"
        
    return estado


