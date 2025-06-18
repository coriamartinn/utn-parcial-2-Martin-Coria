import pygame as pg

def ingresar_nombre(pantalla):
    pg.font.init()
    fuente = pg.font.SysFont("OCR A Extended", 50)
    nombre = ""
    reloj = pg.time.Clock()
    activo = True

    while activo:
        pantalla.fill((0, 0, 0))  # Fondo negro

        texto = fuente.render("Ingrese su nombre (3 letras): " + nombre, True, (255, 255, 255))
        pantalla.blit(texto, (100, 300))

        pg.display.flip()

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                exit()
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN and len(nombre) == 3:
                    activo = False
                elif evento.key == pg.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < 3 and evento.unicode.isalpha():
                    nombre += evento.unicode.upper()

        reloj.tick(30)

    return nombre
