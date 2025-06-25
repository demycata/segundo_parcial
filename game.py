# Module Imports
import pygame as pg

import pygame.mixer as mixer

from funciones import *

# Game Variables

def actualizar_tablero(window, CELLSIZE, grid, celdas_ya_disparadas, celdas_acertadas):
    # Dibuja solo la cuadrícula del jugador
    dibujar_Grilla(window, CELLSIZE, grid, celdas_ya_disparadas, celdas_acertadas)
    
'''
PARA PONER LAS IMAGENES Y QUE CUADRAN QUE LAS CORDENADAS DE LA POS, HACER QUE CUANDO HAGAMOS REC(IMAGEN), PONGASMOS LA POSICION INICIAL EN UNA POS RANDOM
Y QUE LA POS FINAL SEA, SI ES POR EJEMPLO EL BARCO X3, POS INICIAL.X + (50.3) INCLUSIVE
'''

# Player Initialization

# Main Game loop
def start(screen, dificultad, CELLSIZE, ROWS, COLS):
    from assets import sonido_barco, logo_sonidono, logo_sonidosi, sonido_agua

    #ADAPTAR EL JUEGO A LA DIFICULTAD
    CELLSIZE = (CELLSIZE//dificultad)
    ROWS = ROWS * dificultad
    COLS = COLS * dificultad

    #FONDO
    background = pg.image.load('assets\playbackground.png').convert()
    background = pg.transform.scale(background, (820, 600))

    #FUNCIONES DEL JUEGO
    grid = inicializar_matriz(ROWS, COLS, 0)
    celdas_ya_disparadas = []
    celdas_acertadas = []
    cord = generar_cordenas(grid, CELLSIZE)
    barcos = poner_barcos(dificultad, COLS, ROWS, grid, cord)  
    print(barcos)
    mostrar_matriz(grid)
    PUNTOS = 0
    run = True
    #FUNCION MUTEAR
    muted = False

    while run == True:
        screen.blit(background, [0, 0])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            posi = (0, 0)
            impacto = None
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posi = (event.pos)

                    impacto = verificar_disparo(cord, posi, celdas_ya_disparadas, barcos, CELLSIZE, grid, celdas_acertadas)

                    if impacto:
                        PUNTOS += 5
                        print("¡Impacto! Puntos:", PUNTOS)
                        sonido_barco.play()
                        sonido_barco.set_volume(0.1)

                    elif impacto == False:
                        PUNTOS -= 1
                        print("Disparo fallido", PUNTOS)
                        sonido_agua.play()
                        sonido_agua.set_volume(0.1)

                #BOTONES
                    #RESTART
                    if 5 <= posi[0] <= 130 and 135 <= posi[1] <= 159:
                        grid = inicializar_matriz(ROWS, COLS, 0)
                        celdas_ya_disparadas = []
                        celdas_acertadas = []
                        cord = generar_cordenas(grid, CELLSIZE)
                        barcos = poner_barcos(dificultad, COLS, ROWS, grid, cord)
                        PUNTOS = 0
                    #MENU
                    elif 5 <= posi[0] <= 130 and 165 <= posi[1] <= 189:
                        run = False
                    #SONIDO
                    if 0 <= posi[0] <= 40 and 560 <= posi[1] <= 600:
                        muted = not muted
                        if muted:
                            mixer.music.set_volume(0)
                        else:
                            mixer.music.set_volume(0.2)


                          
        PUNTOS += verificar_vida_barcos(barcos)
        mostrar_puntos(PUNTOS, screen)
        estado = verificar_estado_partida(barcos)         
        actualizar_tablero(screen, CELLSIZE, grid, celdas_ya_disparadas, celdas_acertadas)

        if estado:
            run = guardar_score(screen, PUNTOS)

        if muted:
            screen.blit(logo_sonidono, (0, 560))
        else:
            screen.blit(logo_sonidosi, (0, 560))
            
        pg.display.flip()
