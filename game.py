# Module Imports
import pygame as pg

from funciones import *

# Game Variables

def actualizar_tablero(window, CELLSIZE, grid, celdas_ya_disparadas, celdas_acertadas):
    # Dibuja solo la cuadrícula del jugador
    dibujar_Grilla(window, CELLSIZE, grid, celdas_ya_disparadas, celdas_acertadas)
    pg.display.update()

'''
PARA PONER LAS IMAGENES Y QUE CUADRAN QUE LAS CORDENADAS DE LA POS, HACER QUE CUANDO HAGAMOS REC(IMAGEN), PONGASMOS LA POSICION INICIAL EN UNA POS RANDOM
Y QUE LA POS FINAL SEA, SI ES POR EJEMPLO EL BARCO X3, POS INICIAL.X + (50.3) INCLUSIVE
'''

# Player Initialization

# Main Game loop
def start(screen, dificultad, CELLSIZE, ROWS, COLS):
    CELLSIZE = (CELLSIZE//dificultad)
    ROWS = ROWS * dificultad
    COLS = COLS * dificultad
    background = pg.image.load('assets\A567a5185-c250-416f-b093-9cb50ebee91b.jpg').convert()
    background = pg.transform.scale(background, (820, 600))
    grid = inicializar_matriz(ROWS, COLS, 0)
    celdas_ya_disparadas = []
    celdas_acertadas = []
    cord = generar_cordenas(grid, CELLSIZE)
    barcos = poner_barcos(dificultad, COLS, ROWS, grid, cord)  
    print(barcos)
    mostrar_matriz(grid)
    PUNTOS = 0
    while True:
        screen.blit(background, [0, 0])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            posi = (0, 0)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posi = (event.pos)
                    print(posi)
                    impacto = verificar_disparo(cord, posi, celdas_ya_disparadas, barcos, CELLSIZE, grid, celdas_acertadas)
                    if impacto:
                        PUNTOS += 5
                        print("¡Impacto! Puntos:", PUNTOS)
                    elif impacto == False:
                        PUNTOS -= 1
                        print("Disparo fallido", PUNTOS)
        PUNTOS += verificar_vida_barcos(barcos)
        mostrar_puntos(PUNTOS, screen)
        estado = verificar_estado_partida(barcos)         
        actualizar_tablero(screen, CELLSIZE, grid, celdas_ya_disparadas, celdas_acertadas)
        if estado:
            break
