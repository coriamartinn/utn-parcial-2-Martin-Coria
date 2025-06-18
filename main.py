import pygame as pg
import pygame.mixer as mixer

from paquetes.interfaces import *
from paquetes.tablero import *
from paquetes.validates import *


def main() -> None:
    pg.init()
    mixer.init()

    sonido = mixer.Sound("estaticos/sonidos/menu.mp3")
    sonido.set_volume(0)  # Poner volumen 0.4 si querés activarlo
    sonido.play(-1)

    estado = "MENU"
    nivel_actual = "FACIL"
    musica_activada = True
    clock = pg.time.Clock()
    tablero_actual = None
    tablero_disparos = None
    rect_reiniciar = None

    DIMENSIONES = (1024, 768)
    pantalla = pg.display.set_mode(DIMENSIONES)
    pg.display.set_caption("Batalla naval")
    icono_surface = pg.image.load("estaticos/imagenes/icono.png")
    pg.display.set_icon(icono_surface)

    fondo = pg.image.load("estaticos/imagenes/fondo.jpg")
    fondo = pg.transform.scale(fondo, DIMENSIONES)

    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            if evento.type == pg.MOUSEBUTTONDOWN:
                posicion_click = evento.pos
                if estado == "MENU":
                    if rect_jugar and rect_jugar.collidepoint(posicion_click):
                        estado = "JUGAR"
                        tablero_actual = None  # Se creará en la pantalla de juego
                        tablero_disparos = None
                    elif rect_nivel and rect_nivel.collidepoint(posicion_click):
                        estado = "NIVEL"
                    elif rect_puntajes and rect_puntajes.collidepoint(posicion_click):
                        estado = "PUNTAJES"
                    elif rect_salir and rect_salir.collidepoint(posicion_click):
                        estado = "SALIR"
                    elif rect_musica and rect_musica.collidepoint(posicion_click):
                        if musica_activada:
                            mixer.pause()
                            musica_activada = False
                        else:
                            mixer.unpause()
                            musica_activada = True

                elif estado == "NIVEL":
                    if rect_facil and rect_facil.collidepoint(posicion_click):
                        nivel_actual = "FACIL"
                        estado = "MENU"
                    elif rect_medio and rect_medio.collidepoint(posicion_click):
                        nivel_actual = "MEDIO"
                        estado = "MENU"
                    elif rect_dificil and rect_dificil.collidepoint(posicion_click):
                        nivel_actual = "DIFICIL"
                        estado = "MENU"

                elif estado == "JUGAR":
                    if rect_volver and rect_volver.collidepoint(posicion_click):
                        estado = "MENU"
                        tablero_actual = None
                        tablero_disparos = None
                    elif rect_reiniciar and rect_reiniciar.collidepoint(posicion_click):
                        tablero_actual = crear_tablero_con_naves(nivel_actual)
                        tablero_disparos = crear_tablero_vacio(len(tablero_actual))

        pantalla.blit(fondo, (0, 0))

        if estado == "MENU":
            rect_jugar, rect_nivel, rect_puntajes, rect_salir, rect_musica = menu(
                pantalla, nivel_actual
            )

        if estado == "JUGAR":
            if tablero_actual == None:  # Igual que is None pero menos recomendado
                tablero_actual = crear_tablero_con_naves(nivel_actual)
                tablero_disparos = crear_tablero_vacio(len(tablero_actual))
            rect_volver, rect_reiniciar = interfaz_jugar(
                pantalla, nivel_actual, tablero_actual, tablero_disparos
            )

            # Manejar clic en tablero para disparar
            if pg.mouse.get_pressed()[0]:
                posicion = pg.mouse.get_pos()

                # Ignorar clicks en botones volver y reiniciar
                if rect_volver and rect_volver.collidepoint(posicion):
                    pass
                elif rect_reiniciar and rect_reiniciar.collidepoint(posicion):
                    pass
                else:
                    manejar_disparo(tablero_actual, tablero_disparos, posicion, pantalla.get_size())

                if verificar_victoria(tablero_actual, tablero_disparos):
                    print("¡Ganaste!")
                    estado = "MENU"
                    tablero_actual = None
                    tablero_disparos = None

        elif estado == "PUNTAJES":
            interfaz_puntajes(pantalla)

        elif estado == "SALIR":
            pg.quit()
            quit()

        elif estado == "NIVEL":
            rect_facil, rect_medio, rect_dificil = interfaz_nivel(pantalla)

        clock.tick(60)
        pg.display.flip()


if __name__ == "__main__":
    main()
