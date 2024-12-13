import pygame
from funciones import *
from config import *
import pygame.mixer as mixer

pygame.init()
pygame.mixer.init()

tablero_oculto = inicializar_tablero(10)
lista_barcos = colocar_navio(tablero_oculto) 
estado_celdas = inicializar_tablero(10)

texto_input = ""
puntaje = 0

bandera_pantallas = 0
corriendo = True

while corriendo == True:

    if bandera_pantallas == 0:
        mixer.music.set_volume(20)
        ventana.blit(fondo_principal, (0, 0))
        ventana.blit(imagen_jugar, boton_jugar)
        ventana.blit(imagen_nivel, boton_nivel)
        ventana.blit(imagen_puntaje, boton_puntaje)
        ventana.blit(imagen_salir, boton_salir)


    elif bandera_pantallas == 1:        #click en boton jugar
        ventana.blit(fondo, (0, 0))
        ventana.blit(imagen_reiniciar, boton_reiniciar)
        ventana.blit(imagen_volver, boton_volver)
        ventana.blit(imagen_puntos, (5, 5))
        texto_puntos = fuente.render(f"Puntos: {puntaje}", False, BLANCO, None)
        ventana.blit(texto_puntos, (15, 20))

        if texto_input:
            mostrar_texto(f"Nombre: {texto_input}", 300, 10)

        coordenadas_rect = dibujar_tablero(ventana, tablero_oculto, 10)
        ocultador_tablero(ventana, coordenadas_rect, estado_celdas)
        
    elif bandera_pantallas == 2:        #click en boton ver puntajes
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_volver, boton_volver)
        puntajes = guardar_puntajes("puntajes.csv")
        mostrar_puntajes(puntajes, 10, 10)

    elif bandera_pantallas == 3:     # boton nivel
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_facil, boton_facil)
        ventana.blit(imagen_medio, boton_medio)
        ventana.blit(imagen_dificil, boton_dificil)
        ventana.blit(imagen_volver, boton_volver)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

        if event.type == pygame.TEXTINPUT:
            texto_input = generar_texto_input(event.text, texto_input, "tecla_letra")

        elif event.type == pygame.KEYDOWN and bandera_pantallas == 1:
            if event.key == pygame.K_BACKSPACE:
                texto_input = generar_texto_input(event.key, texto_input, "tecla_borrar")
            
            if event.key == pygame.K_RETURN: 
                print(f"Nombre del jugador: {texto_input}")  
                crear_archivo_puntaje(texto_input, puntaje)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            #print(pos_mouse)
            if bandera_pantallas == 0:
                if boton_salir.collidepoint(pos_mouse):
                    corriendo = False

                elif boton_jugar.collidepoint(pos_mouse):
                    bandera_pantallas = 1
                
                elif boton_puntaje.collidepoint(pos_mouse):
                    bandera_pantallas = 2
                
                elif boton_nivel.collidepoint(pos_mouse):
                    bandera_pantallas = 3
                
                if boton_usuario.collidepoint(pos_mouse):
                    pass

            elif bandera_pantallas == 1:
                for i in range(len(tablero_oculto)):
                    for j in range(len(tablero_oculto[0])):
                        if coordenadas_rect[i][j].collidepoint(pos_mouse) and estado_celdas[i][j] == False:
                            estado_celdas[i][j] = True
                            if tablero_oculto[i][j] == 0:
                                puntaje -= 1
                                
                            elif tablero_oculto[i][j] != 0:
                                puntaje += 5
                                valor = gestionar_barcos(tablero_oculto, estado_celdas, lista_barcos)
                                if valor > 0:
                                    puntaje += valor * 10
                            print(puntaje)

                            
                if boton_reiniciar.collidepoint(pos_mouse):   # resetear barcos
                    
                    tablero_oculto = inicializar_tablero(10)
                    estado_celdas = inicializar_tablero(10)
                    puntaje = 0
                    texto_input = ""
                    colocar_navio(tablero_oculto)

                    dibujar_tablero(ventana, coordenadas_rect, 10)
                    ocultador_tablero(ventana, coordenadas_rect, estado_celdas)
                    
                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0


            elif bandera_pantallas == 2:
                if boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0
            
            elif bandera_pantallas == 3:
                if boton_facil.collidepoint(pos_mouse):
                    bandera_pantallas = 1

                elif boton_medio.collidepoint(pos_mouse):
                    bandera_pantallas = 1

                elif boton_dificil.collidepoint(pos_mouse):
                    bandera_pantallas = 1
                    
                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0


    pygame.display.flip()

pygame.quit()
