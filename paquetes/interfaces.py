import pygame as pg


from paquetes.tablero import *


import pygame as pg

def menu(pantalla: pg.display, nivel_actual="FACIL"):
    jugar = "Jugar"
    nivel = "Nivel"
    puntaje = "Puntajes"
    salir = "Salir"
    musica = "On/Off"
    padding_x = 20
    padding_y = 15

    pg.font.init()
    fuente = pg.font.SysFont("OCR A Extended", 45)
    fuente_alternativa = pg.font.SysFont("OCR A Extended", 25)

    # Superficies de texto
    superficie_jugar = fuente.render(jugar, True, (255, 255, 255))
    superficie_nivel = fuente.render(nivel, True, (255, 255, 255))
    superficie_puntaje = fuente.render(puntaje, True, (255, 255, 255))
    superficie_salir = fuente.render(salir, True, (255, 255, 255))
    superficie_musica = fuente_alternativa.render(musica, True, (255, 255, 255))

    # Obtener rects
    rect_jugar = superficie_jugar.get_rect()
    rect_nivel = superficie_nivel.get_rect()
    rect_puntajes = superficie_puntaje.get_rect()
    rect_salir = superficie_salir.get_rect()
    rect_musica = superficie_musica.get_rect()

    # Centrar posiciones
    rect_jugar.center = (512, 284)
    rect_nivel.center = (512, 384)
    rect_puntajes.center = (512, 484)
    rect_salir.center = (512, 584)
    rect_musica.center = (959, 726)

    # Fondos con padding
    fondo_jugar = pg.Rect(rect_jugar.left - padding_x, rect_jugar.top - padding_y, rect_jugar.width + 2*padding_x, rect_jugar.height + 2*padding_y)
    fondo_nivel = pg.Rect(rect_nivel.left - padding_x, rect_nivel.top - padding_y, rect_nivel.width + 2*padding_x, rect_nivel.height + 2*padding_y)
    fondo_puntajes = pg.Rect(rect_puntajes.left - padding_x, rect_puntajes.top - padding_y, rect_puntajes.width + 2*padding_x, rect_puntajes.height + 2*padding_y)
    fondo_salir = pg.Rect(rect_salir.left - padding_x, rect_salir.top - padding_y, rect_salir.width + 2*padding_x, rect_salir.height + 2*padding_y)
    fondo_musica = pg.Rect(rect_musica.left - padding_x, rect_musica.top - padding_y, rect_musica.width + 2*padding_x, rect_musica.height + 2*padding_y)

    # Dibujar fondos
    color_fondo = (4, 6, 88)
    pg.draw.rect(pantalla, color_fondo, fondo_jugar, border_radius=15)
    pg.draw.rect(pantalla, color_fondo, fondo_nivel, border_radius=15)
    pg.draw.rect(pantalla, color_fondo, fondo_puntajes, border_radius=15)
    pg.draw.rect(pantalla, color_fondo, fondo_salir, border_radius=15)
    pg.draw.rect(pantalla, color_fondo, fondo_musica, border_radius=15)

    # Dibujar textos
    pantalla.blit(superficie_jugar, rect_jugar)
    pantalla.blit(superficie_nivel, rect_nivel)
    pantalla.blit(superficie_puntaje, rect_puntajes)
    pantalla.blit(superficie_salir, rect_salir)
    pantalla.blit(superficie_musica, rect_musica)

    # Retornamos todos los rects para control de clics
    return rect_jugar, rect_nivel, rect_puntajes, rect_salir, rect_musica



def interfaz_jugar(pantalla: pg.display, nivel="FACIL", tablero=None, tablero_disparos=None):
    """
    Esta funcion se encarga de dibujar en pantalla la interfaz del interfaz principal
    Args:
        pantalla (pg.display): Recibe el display de pantalla
    Returns:
        None: No existe retorno
    """    
    if nivel != "FACIL" and nivel != "MEDIO" and nivel != "DIFICIL":
        nivel = "FACIL"

    if tablero is None:
        tablero = crear_tablero_con_naves(nivel)
    if tablero_disparos is None:
        tablero_disparos = crear_tablero_vacio(len(tablero))

    imprimir_tablero(pantalla, tablero, tablero_disparos)

    # Botón Volver
    pg.font.init()
    fuente = pg.font.SysFont("OCR A Extended", 30)
    texto_volver = fuente.render("Volver", True, (255, 255, 255))
    rect_volver = texto_volver.get_rect(center=(955, 700))
    fondo_volver = pg.Rect(rect_volver.left - 10, rect_volver.top - 10,
                          rect_volver.width + 20, rect_volver.height + 20)
    pg.draw.rect(pantalla, (88, 6, 6), fondo_volver, border_radius=12)
    pantalla.blit(texto_volver, rect_volver)

    # Botón Reiniciar
    texto_reiniciar = fuente.render("Reiniciar", True, (255, 255, 255))
    rect_reiniciar = texto_reiniciar.get_rect(center=(955, 760))
    fondo_reiniciar = pg.Rect(rect_reiniciar.left - 10, rect_reiniciar.top - 10,
                             rect_reiniciar.width + 20, rect_reiniciar.height + 20)
    pg.draw.rect(pantalla, (6, 88, 6), fondo_reiniciar, border_radius=12)
    pantalla.blit(texto_reiniciar, rect_reiniciar)

    return fondo_volver, fondo_reiniciar



def interfaz_puntajes(pantalla: pg.display) -> None:
    """
    Esta funcion se encarga de dibujar en pantalla la interfaz del interfaz principal
    Args:
        pantalla (pg.display): Recibe el display de pantalla
    Returns:
        None: No existe retorno
    """
    jugar = "PRUEBA2"
    puntaje = "Prueba2"
    salir = "Saliraa2"

    pg.font.init()
    fuente = pg.font.SysFont("Arial", 45)
    superficie_jugar = fuente.render(jugar, True, (0, 0, 0))
    superficie_puntaje = fuente.render(puntaje, True, (0, 0, 0))
    superficie_salir = fuente.render(salir, True, (0, 0, 0))

    # Obtengo el RECT de la superficie
    rect_jugar = superficie_jugar.get_rect()
    rect_puntaje = superficie_puntaje.get_rect()
    rect_salir = superficie_salir.get_rect()

    # Centro la posicion de la superficie ->(texto creado)
    rect_jugar.center = (512, 384)
    rect_puntaje.center = (512, 484)
    rect_salir.center = (512, 584)

    pantalla.blit(superficie_jugar, rect_jugar)
    pantalla.blit(superficie_puntaje, rect_puntaje)
    pantalla.blit(superficie_salir, rect_salir)

def interfaz_nivel(pantalla: pg.display):
    # Dibuja tres botones: Fácil, Medio, Difícil
    # Devuelve los rects de esos botones para detectar clicks

    pg.font.init()
    fuente = pg.font.SysFont("Arial", 40)
    facil = fuente.render("Fácil", True, (255, 255, 255))
    medio = fuente.render("Medio", True, (255, 255, 255))
    dificil = fuente.render("Difícil", True, (255, 255, 255))

    rect_facil = facil.get_rect(center=(400, 150))
    rect_medio = medio.get_rect(center=(400, 250))
    rect_dificil = dificil.get_rect(center=(400, 350))

    pantalla.fill((0, 0, 0))  # Fondo negro

    pantalla.blit(facil, rect_facil)
    pantalla.blit(medio, rect_medio)
    pantalla.blit(dificil, rect_dificil)

    return rect_facil, rect_medio, rect_dificil

def mostrar_selector_nivel(pantalla: pg.Surface) -> tuple:
    """
    Dibuja la pantalla de selección de nivel y retorna los rects para detectar clics.
    """
    pg.font.init()
    fuente = pg.font.SysFont("OCR A Extended", 40)

    opciones = {
        "FACIL": fuente.render("FACIL", True, (255, 255, 255)),
        "MEDIO": fuente.render("MEDIO", True, (255, 255, 255)),
        "DIFICIL": fuente.render("DIFICIL", True, (255, 255, 255)),
    }

    rects = {}
    y = 180
    for nombre, superficie in opciones.items():
        rect = superficie.get_rect(center=(400, y))
        fondo = pg.Rect(rect.left - 20, rect.top - 15, rect.width + 40, rect.height + 30)
        pg.draw.rect(pantalla, (50, 50, 200), fondo, border_radius=10)
        pantalla.blit(superficie, rect)
        rects[nombre] = rect
        y += 100

    return rects["FACIL"], rects["MEDIO"], rects["DIFICIL"]

def verificar_victoria(tablero, tablero_disparos):
    victoria = True
    for fila in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[fila][col] == 1 and tablero_disparos[fila][col] == 0:
                victoria = False
    return victoria

