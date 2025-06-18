import random
import string

import pygame as pg


NIVELES = {
    "FACIL": {
        "tamano": 10,
        "tipos_naves": {
            "submarino": (1, 4),
            "destructor": (2, 3),
            "crucero": (3, 2),
            "acorazado": (4, 1),
        },
    },
    "MEDIO": {
        "tamano": 20,
        "tipos_naves": {
            "submarino": (1, 8),  # el doble de cada tipo
            "destructor": (2, 6),
            "crucero": (3, 4),
            "acorazado": (4, 2),
        },
    },
    "DIFICIL": {
        "tamano": 30,
        "tipos_naves": {
            "submarino": (1, 12),  # el triple de cada tipo
            "destructor": (2, 9),
            "crucero": (3, 6),
            "acorazado": (4, 3),
        },
    },
}


def crear_tablero_vacio(tamano):
    tablero = []
    for _ in range(tamano):
        fila = []
        for _ in range(tamano):
            fila.append(0)
        tablero.append(fila)
        
    return tablero


def es_posicion_valida(tablero, fila, col, tamaño, orientacion):
    es_valida = False
    if orientacion == "horizontal":
        if col + tamaño <= len(tablero[0]):
            es_valida = all(tablero[fila][c] == 0 for c in range(col, col + tamaño))
    else:
        if fila + tamaño <= len(tablero):
            es_valida = all(tablero[r][col] == 0 for r in range(fila, fila + tamaño))
    return es_valida


def colocar_nave(tablero, tamaño):
    max_intentos = 100
    exito = False  # Variable para controlar si se colocó o no

    for _ in range(max_intentos):
        fila = random.randint(0, len(tablero) - 1)
        col = random.randint(0, len(tablero[0]) - 1)
        orientacion = random.choice(["horizontal", "vertical"])
        if es_posicion_valida(tablero, fila, col, tamaño, orientacion):
            if orientacion == "horizontal":
                for c in range(col, col + tamaño):
                    tablero[fila][c] = 1
            else:
                for r in range(fila, fila + tamaño):
                    tablero[r][col] = 1
            exito = True
            break  # Salimos del for porque ya colocamos la nave
    return exito


def crear_tablero_con_naves(nivel="FACIL"):
    if nivel == "FACIL":
        dificultad = NIVELES["FACIL"]
    elif nivel == "MEDIO":
        dificultad = NIVELES["MEDIO"] 
    elif nivel == "DIFICIL":
        dificultad = NIVELES["DIFICIL"]

    tablero = crear_tablero_vacio(dificultad["tamano"])
    for tipo, (tamaño, cantidad) in dificultad["tipos_naves"].items():
        colocadas = 0
        for _ in range(cantidad):
            if colocar_nave(tablero, tamaño):
                colocadas += 1
        if colocadas < cantidad:
            print(f"Advertencia: no se colocaron todas las naves de tipo {tipo}")
    return tablero


#def imprimir_tablero(pantalla, tablero, tablero_disparos=None):
    if tablero_disparos is None:
        tablero_disparos = crear_tablero_vacio(len(tablero))

    pg.font.init()
    margen_izquierdo = 40
    margen_arriba = 40
    ancho_pantalla, alto_pantalla = pantalla.get_size()
    tamano_celda = min(
        (ancho_pantalla - 2 * margen_izquierdo) // len(tablero[0]),
        (alto_pantalla - 2 * margen_arriba) // len(tablero),
    )

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            calcular_x = margen_izquierdo + columna * tamano_celda
            calcular_y = margen_arriba + fila * tamano_celda

            if tablero_disparos[fila][columna] == 1:
                if tablero[fila][columna] == 1:
                    color_celda = (255, 0, 0)  # impacto (rojo)
                else:
                    color_celda = (0, 0, 255)  # agua (azul)
            else:
                if tablero[fila][columna] == 1:
                    color_celda = (0, 255, 0)  # mostrar nave (verde)
                else:
                    color_celda = (200, 200, 255)  # sin disparar (celda clara)


            pg.draw.rect(pantalla, color_celda, (calcular_x, calcular_y, tamano_celda, tamano_celda))
            pg.draw.rect(pantalla, (0, 0, 0), (calcular_x, calcular_y, tamano_celda, tamano_celda), 1)


def manejar_disparo(tablero, tablero_disparos, posicion, dimension_pantalla):
    margen_izquierdo = 40
    margen_arriba = 40
    ancho_pantalla, alto_pantalla = dimension_pantalla
    espacio_disponible_x = ancho_pantalla - 2 * margen_izquierdo
    espacio_disponible_y = alto_pantalla - 2 * margen_arriba
    tamano_celda = min(espacio_disponible_x // len(tablero[0]), espacio_disponible_y // len(tablero))

    x, y = posicion
    columna = (x - margen_izquierdo) // tamano_celda
    fila = (y - margen_arriba) // tamano_celda

    exito = False
    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
        if tablero_disparos[fila][columna] == 0:
            tablero_disparos[fila][columna] = 1
            exito = True

    return exito

def imprimir_tablero(pantalla, tablero, tablero_disparos=None):
    if tablero_disparos is None:
        tablero_disparos = crear_tablero_vacio(len(tablero))

    pg.font.init()
    margen_izquierdo = 60  # Más margen para las letras
    margen_arriba = 60     # Más margen para los números
    ancho_pantalla, alto_pantalla = pantalla.get_size()
    tamano_celda = min(
        (ancho_pantalla - 2 * margen_izquierdo) // len(tablero[0]),
        (alto_pantalla - 2 * margen_arriba) // len(tablero),
    )

    fuente = pg.font.SysFont("Arial", tamano_celda // 2)

    # Dibujar números columnas arriba
    for col in range(len(tablero[0])):
        numero = str(col + 1)
        texto_numero = fuente.render(numero, True, (255, 255, 255))
        x = margen_izquierdo + col * tamano_celda + tamano_celda // 2 - texto_numero.get_width() // 2
        y = margen_arriba // 2 - texto_numero.get_height() // 2
        pantalla.blit(texto_numero, (x, y))

    # Letras filas a la izquierda
    letras = string.ascii_uppercase
    for fila in range(len(tablero)):
        letra = letras[fila] if fila < len(letras) else "?"
        texto_letra = fuente.render(letra, True, (255, 255, 255))
        x = margen_izquierdo // 2 - texto_letra.get_width() // 2
        y = margen_arriba + fila * tamano_celda + tamano_celda // 2 - texto_letra.get_height() // 2
        pantalla.blit(texto_letra, (x, y))

    # Dibujar celdas
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            calcular_x = margen_izquierdo + columna * tamano_celda
            calcular_y = margen_arriba + fila * tamano_celda

            if tablero_disparos[fila][columna] == 1:
                if tablero[fila][columna] == 1:
                    color_celda = (255, 0, 0)  # impacto (rojo)
                else:
                    color_celda = (0, 0, 255)  # agua (azul)
            else:
                color_celda = (200, 200, 255)  # sin disparar (celda clara)

            pg.draw.rect(pantalla, color_celda, (calcular_x, calcular_y, tamano_celda, tamano_celda))
            pg.draw.rect(pantalla, (0, 0, 0), (calcular_x, calcular_y, tamano_celda, tamano_celda), 1)