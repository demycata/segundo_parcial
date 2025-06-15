# Module Imports
import pygame as pg

import settings as config

from BibliotecaDemy import *

from funciones import *

# Initialization
pg.init()

# Game Assets

# Game Utility Functions

# Game Settings

ROWS = 10
COLS = 10
CELLSIZE = 45

# Colors

# Display

screen = pg.display.set_mode((config.SCREENWIDTH, config.SCREENHEIGHT))


# Game Lists/Dics

# Game Variables

def updateGameScreen(window, CELLSIZE, grid, celdas_ya_disparadas):
    #window.fill((0, 0, 0))
    # Dibuja solo la cuadrícula del jugador
    dibujar_Grilla(window, CELLSIZE, grid, celdas_ya_disparadas)
    pg.display.update()

# Game Functions


'''
PARA PONER LAS IMAGENES Y QUE CUADRAN QUE LAS CORDENADAS DE LA POS, HACER QUE CUANDO HAGAMOS REC(IMAGEN), PONGASMOS LA POSICION INICIAL EN UNA POS RANDOM
Y QUE LA POS FINAL SEA, SI ES POR EJEMPLO EL BARCO X3, POS INICIAL.X + (50.3) INCLUSIVE
'''




# Game Sounds

# Player Initialization

# Main Game loop
def jugar(dificultad, CELLSIZE, ROWS, COLS):
    background = pg.image.load('assets\A567a5185-c250-416f-b093-9cb50ebee91b.jpg').convert()
    background = pg.transform.scale(background, (831, 600))
    grid = inicializar_matriz((ROWS * dificultad), (COLS * dificultad), 0)
    celdas_ya_disparadas = []
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
                    impacto = verificar_disparo(cord, posi, celdas_ya_disparadas, barcos, CELLSIZE, grid)
                    if impacto:
                        PUNTOS += 5
                        print("¡Impacto! Puntos:", PUNTOS)
                    elif impacto == False:
                        PUNTOS -= 1
                        print("Disparo fallido", PUNTOS)
        PUNTOS += verificar_vida_barcos(barcos)
        estado = verificar_estado_partida(barcos)         
        updateGameScreen(screen, CELLSIZE, grid, celdas_ya_disparadas)
        if estado:
            break

jugar(1, config.CELLSIZE, config.ROWS, config.COLS)