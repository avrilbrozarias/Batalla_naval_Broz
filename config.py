import pygame
import pygame.mixer as mixer

pygame.init()
pygame.mixer.init()

ANCHO_VENTANA = 900
ALTO_VENTANA = 650

ANCHO_BOTON = 200
ALTO_BOTON = 70

CENTRO_BOTON_X = (ANCHO_VENTANA / 2) - (ANCHO_BOTON / 2)



#COLOR_FONDO = (20, 50, 153)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (70,70,70)
AZUL = (34, 69, 179)
ROJO = (231, 30, 30)

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
mixer.music.load("assets\\sounds\\musica_fondo.mp3")
#mixer.music.play()
ruido_bomba = mixer.Sound("assets\\sounds\\efecto_bomba.mp3")
ruido_bomba.set_volume(0.3)

icono = pygame.image.load("assets\\img\\logo3.jpg")
pygame.display.set_icon(icono)

pygame.display.set_caption("Batalla Naval")

fondo_principal = pygame.image.load("assets\\img\\fondo1.jpg")
fondo_principal = pygame.transform.scale(fondo_principal, (ANCHO_VENTANA, ALTO_VENTANA))

fondo = pygame.image.load("assets\\img\\fondo2.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

fondo_puntajes = pygame.image.load("assets\\img\\fondo.jpg")
fondo_puntajes = pygame.transform.scale(fondo_puntajes, (ANCHO_VENTANA, ALTO_VENTANA))

fuente = pygame.font.SysFont("Consola", 25, bold = False)

imagen_usuario = pygame.image.load("assets\\img\\fondo_boton.png")
imagen_nivel = pygame.image.load("assets\\img\\nivel.png")
imagen_jugar = pygame.image.load("assets\\img\\jugar.png")
imagen_puntaje = pygame.image.load("assets\\img\\ver_puntaje.png")
imagen_salir = pygame.image.load("assets\\img\\salir.png")
imagen_reiniciar = pygame.image.load("assets\\img\\reiniciar.png")
imagen_volver = pygame.image.load("assets\\img\\volver.png")
imagen_facil = pygame.image.load("assets\\img\\facil.png")
imagen_medio = pygame.image.load("assets\\img\\medio.png")
imagen_dificil = pygame.image.load("assets\\img\\dificil.png")
imagen_puntos = pygame.image.load("assets\\img\\fondo_boton.png")

imagen_usuario = pygame.transform.scale(imagen_puntos, (ANCHO_BOTON + 30, ALTO_BOTON - 20))
imagen_nivel = pygame.transform.scale(imagen_nivel, (ANCHO_BOTON, ALTO_BOTON))
imagen_jugar = pygame.transform.scale(imagen_jugar, (ANCHO_BOTON, ALTO_BOTON))
imagen_puntaje = pygame.transform.scale(imagen_puntaje, (ANCHO_BOTON, ALTO_BOTON))
imagen_salir = pygame.transform.scale(imagen_salir, (ANCHO_BOTON, ALTO_BOTON))
imagen_reiniciar = pygame.transform.scale(imagen_reiniciar, (ANCHO_BOTON - 60, ALTO_BOTON - 20))
imagen_volver = pygame.transform.scale(imagen_volver, (ANCHO_BOTON - 60, ALTO_BOTON - 20))
imagen_facil = pygame.transform.scale(imagen_facil, (ANCHO_BOTON, ALTO_BOTON))
imagen_medio = pygame.transform.scale(imagen_medio, (ANCHO_BOTON, ALTO_BOTON))
imagen_dificil = pygame.transform.scale(imagen_dificil, (ANCHO_BOTON, ALTO_BOTON))
imagen_puntos = pygame.transform.scale(imagen_puntos, (ANCHO_BOTON - 60, ALTO_BOTON - 20))

boton_usuario = imagen_usuario.get_rect()
boton_usuario.x = 0
boton_usuario.y = 0

boton_jugar = imagen_jugar.get_rect()
boton_jugar.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_jugar.y = (ALTO_VENTANA / 6)

boton_nivel = imagen_nivel.get_rect()
boton_nivel.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_nivel.y = (ALTO_VENTANA / 3)

boton_puntaje = imagen_puntaje.get_rect()
boton_puntaje.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_puntaje.y = (ALTO_VENTANA / 2)

boton_salir = imagen_salir.get_rect()
boton_salir.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_salir.y = (ALTO_VENTANA - ALTO_VENTANA / 3)

boton_volver = imagen_reiniciar.get_rect()
boton_volver.x = 755
boton_volver.y = 590

boton_reiniciar = imagen_reiniciar.get_rect()
boton_reiniciar.x = 3
boton_reiniciar.y = 590

boton_facil = imagen_facil.get_rect()
boton_facil.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_facil.y = (ALTO_VENTANA / 6)

boton_medio = imagen_medio.get_rect()
boton_medio.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_medio.y = (ALTO_VENTANA / 3)

boton_dificil = imagen_dificil.get_rect()
boton_dificil.x = (ANCHO_VENTANA / 2 - ANCHO_BOTON / 2)
boton_dificil.y = (ALTO_VENTANA / 2)


