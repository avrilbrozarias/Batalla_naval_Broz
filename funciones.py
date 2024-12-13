import pygame
import random
from config import *

pygame.init()

def inicializar_tablero(dificultad:int, valor = False)->list:
    '''
    Inicializa una matriz vacia y la retorna.
    '''
    matriz = []
    for _ in range(dificultad):
        fila = []
        matriz += [fila]
        for _ in range(dificultad):
            fila += [valor]
    return matriz

def mostrar_matriz(matriz:list)->None:
    '''
    Recibe una matriz, la recorre y la muestra.
    No retorna nada
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],  end=" ")
        print("")
        
    
def colocar_navio(matriz:list)->list:
    """
    Recibe una matriz,  y coloca los barcos. Retorna la lista de barcos colocados y su valor. 
    """
    lista_barcos_colocados = []

    cant_submarino = 4
    cant_destructores = 3
    cant_cruceros = 2
    cant_acorazados = 1
        
    lista_valor = [1, 2, 3, 4]
    lista_tipos = ["submarino", "destructor", "crucero", "acorazado"]
    lista_cantidades = [cant_submarino, cant_destructores, cant_cruceros, cant_acorazados]

    for i in range(len(lista_tipos)):

        contador_colocados = 0

        while  contador_colocados < lista_cantidades[i]:

            fila_inicial = random.randint(0, len(matriz) - (lista_valor[i]))
            columna_inicial = random.randint(0, len(matriz[0]) - (lista_valor[i]))
            orientacion = random.choice(["H", "V"])
            lista_barco = []
            if validar_casilleros(matriz, fila_inicial, columna_inicial, lista_valor[i], orientacion) == True:
                contador_colocados += 1
                for j in range(lista_valor[i]):
                    if orientacion == "H":
                        matriz[fila_inicial][columna_inicial + j] = lista_valor[i]
                        bloque_barco = {"fila": fila_inicial, "columna": columna_inicial + j, "valor": lista_valor[i], "tocado": False, "hundido" : False }
                    else:
                        matriz[fila_inicial + j][columna_inicial] = lista_valor[i]
                        bloque_barco = {"fila": fila_inicial + j, "columna": columna_inicial, "valor": lista_valor[i], "tocado": False, "hundido" : False }
                    
                    lista_barco.append(bloque_barco)
            
                lista_barcos_colocados.append(lista_barco)

    return lista_barcos_colocados


def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto (H o V)
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) <= len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) <= len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio

def dibujar_tablero(ventana, matriz:list, dificultad:int):
    '''
    Recibe una matriz por parametro y la recorre y crea un rectangulo de color segun corresponda.
    Devuelve una matriz con las ubicaciones de los rectangulos.
    '''

    if dificultad == 10:
        tam_celda = 40
    elif dificultad == 20:
        tam_celda = 25
    else:
        tam_celda = 15

    ancho_tablero = tam_celda * dificultad
    mitad_tablero_x = ancho_tablero // 2
    eje_x_centrado = (ANCHO_VENTANA // 2) - mitad_tablero_x
    
    alto_tablero = tam_celda * dificultad
    mitad_tablero_y = alto_tablero // 2
    eje_y_centrado = (ALTO_VENTANA // 2) - mitad_tablero_y

    matriz_rectangulos = inicializar_tablero(dificultad)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            eje_x = j * tam_celda
            eje_y = i * tam_celda

            rectangulo = pygame.Rect(eje_x_centrado + eje_x, eje_y_centrado + eje_y, tam_celda, tam_celda)
            
            matriz_rectangulos[i][j] = rectangulo
            valor_barco = matriz[i][j]

            if valor_barco == 0:
                color = AZUL
            else:
                color = ROJO
            pygame.draw.rect(ventana, color, rectangulo)


    return matriz_rectangulos

def ocultador_tablero(ventana, matriz_rectangulos:list, estado_casillero:list):
    '''
    Recibe la matriz con las coordenadas de los rectangulos del tablero y su estado. 
    Si el estado es True, el ancho del rectangulo cambia su valor.
    '''

    for i in range(len(matriz_rectangulos)):
        for j in range(len(matriz_rectangulos[0])):
            rectangulo = matriz_rectangulos[i][j]
            estado_ocultador = estado_casillero[i][j]

            if estado_ocultador == True:
                ocultador = 2
            else:
                ocultador = 0
        
            pygame.draw.rect(ventana, GRIS, rectangulo, width = ocultador)
            pygame.draw.rect(ventana, NEGRO, rectangulo, width = 2)

def gestionar_barcos(tablero:list, matriz_estado:list, lista_barcos:list)->int:
    '''
    Recibe la matriz principal, la lista con los barcos colocados, la lista de estado de los barcos.
    Verifica si el barco fue hundido y retorna el largo del barco.

    '''
    valor_hundido = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):

            verificar_barcos(lista_barcos, i, j, matriz_estado[i][j])
            largo_hundido = verificar_estado_barcos(lista_barcos)

            if largo_hundido >= 1:
                valor_hundido = largo_hundido
                break

    return valor_hundido

def verificar_barcos(lista_barcos:list, fila:int, columna:int, matriz_estado:list)->None:
    '''
    Recibe la lista de los barcos colocados, un indice especifico y la lista de estados de los barcos(True o False).
    Verificar si un disparo en la posición específica del tablero toco un barco.
    No tiene retorno.
    '''

    for i in range(len(lista_barcos)):
        for j in range(len(lista_barcos[i])):

            fila_bloque = lista_barcos[i][j]["fila"]
            columna_bloque = lista_barcos[i][j]["columna"]

            if (fila == fila_bloque) and (columna == columna_bloque) and (matriz_estado == True):

                lista_barcos[i][j]["tocado"] = True


def verificar_estado_barcos(lista_barcos:list)->int:
    '''
    Recibe por parametro la lista de los barcos colocados.
    Verifica si un barco fue hundido, en caso de serlo retorna el largo del barco.
    '''
    valor = 0
    bandera_tocado = False
    for i in range(len(lista_barcos)):
        for j in range(len(lista_barcos[i])):

            if lista_barcos[i][j]["tocado"] == True and lista_barcos[i][j]["hundido"] == False:
                bandera_tocado = True
            else:
                break

        if bandera_tocado == True:
            lista_barcos[i][j]["hundido"] = True
            valor = lista_barcos[i][j]["valor"]
            break

    return valor

def generar_texto_input(input:str, texto:str, input_key:str):
    '''
    Recibe los caracteres que escribe el usuario, el nombre generado y el tipo de tecla presionado.
    Genera un string con el caracter ingresado y lo retorna
    '''
    texto_input = texto 
    if input_key == "tecla_letra":
        len_text_input = len(texto)
        if len_text_input < 20:
            texto_input += input
            texto_input = texto_input.capitalize()
    else:
        texto_input = texto_input[0:len(texto_input)-1]
    
    return texto_input


def mostrar_texto(texto, x, y):
    superficie = fuente.render(texto, True, BLANCO)
    ventana.blit(superficie, (x, y))


def crear_archivo_puntaje(texto_input, puntaje):
    '''
    Recibe el nombre del jugador y su puntaje.
    Crea un archivo csv con los datos
    '''
    with open("puntajes.csv", "a") as usuarios:
        usuarios.write(f"{texto_input},{puntaje}\n")


def guardar_puntajes(usuarios):
    '''
    Lee el archivo CSV y separa los datos de los jugadores
    '''
    with open("puntajes.csv", "r") as usuarios:
        contenido = usuarios.read()

        lista_usuarios = contenido.split("\n")
        
        lista_jugadores = []

        for i in range(1, len(lista_usuarios) - 1):
            lista_datos = lista_usuarios[i].split(",")
            
            nombre, puntaje = lista_datos

            lista_jugadores.append({"Nombre" : nombre, "Puntaje" : puntaje})


    return lista_jugadores

def ordenar_puntajes(lista_jugadores):

    for i in range(len(lista_jugadores) - 1):
        for j in range(i + 1, len(lista_jugadores)):
            if int(lista_jugadores[i]["Puntaje"]) < int(lista_jugadores[j]["Puntaje"]):
                aux = lista_jugadores[i]
                lista_jugadores[i] = lista_jugadores[j]
                lista_jugadores[j] = aux
    return lista_jugadores


def mostrar_puntajes(puntajes, x, y):
    '''
    Recibe la lista de los puntajes y los muestra por pantalla.
    '''
    fuente = pygame.font.Font(None, 24)
    puntajes_ordenados = ordenar_puntajes(puntajes)

    for puntaje in puntajes_ordenados:
        texto_clave = fuente.render(f"{puntaje["Nombre"]}:", True, BLANCO)
        texto_valor = fuente.render(puntaje["Puntaje"], True, BLANCO)

        ventana.blit(texto_clave, (x, y))
        y += 20
        ventana.blit(texto_valor, (x, y))
        y += 20








