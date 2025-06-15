
import pygame as pg

import random

def generar_cordenas(grid, CELLSIZE):
    cord = []
    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        fila = []
        for j in range(len(grid[i])):
            pos_x = start_x + j * CELLSIZE
            pos_y = start_y + i * CELLSIZE
            fila.append((pos_x, pos_y))
        cord.append(fila)
    return cord

def dibujar_Grilla(display, cellsize, grid, celdas_ya_disparadas):
    """Dibuja solo la cuadrícula del jugador en la pantalla"""

    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos_x = start_x + j * cellsize
            pos_y = start_y + i * cellsize
            if (pos_x, pos_y) in celdas_ya_disparadas: # ROJO si ya estan disparadas
                pg.draw.rect(display, 'red', (pos_x, pos_y, cellsize, cellsize), 1)
            else:   # si no las pone en blanco
                pg.draw.rect(display, 'green', (pos_x, pos_y, cellsize, cellsize), 1)

def cords_barco(grid, tam_barco, cord, columnas, filas):
    """
    Coloca un barco horizontal de tamaño tam_barco en una fila aleatoria,
    verificando que haya espacio suficiente (solo ceros).
    """
    colocado = False
    coords_barco = []

    while colocado == False:
        fila = random.randint(0, filas - tam_barco)
        col_inicio = random.randint(0, columnas - 1)
        # Verifica si hay espacio suficiente
        espacio_libre = verifica_espacio_libre(tam_barco, grid, col_inicio, fila)
        if espacio_libre == True:
            for i in range(tam_barco):
                grid[fila + i][col_inicio] = 1
                coords_barco.append((cord[fila + i][col_inicio]))
            colocado = True

    return coords_barco    
    
def generar_barcos(grid, cord, barco, cant, dificultad, barcos, COLS, ROWS):
    for i in range(cant*dificultad):
        barco_dic = {}
        cords = cords_barco(grid, barco, cord, COLS, ROWS)
        barco_dic['Cordenadas'] = cords
        barco_dic['Tam'] = barco
        barco_dic['Vida'] = barco
        print(barco_dic)
        barcos.append(barco_dic)

def poner_barcos(dificultad, COLS, ROWS, grid, cord):
    barcos = []
    # CANTIDAD DE CASILLAS QUE OCUPAN
    submarionos = 1
    destructors = 2
    cruceros = 3
    acorazado = 4
    # CANTIDAD DE BARCOS
    cant_submarionos = 4
    cant_destructors = 3
    cant_cruceros = 2
    cant_acorazado = 1
    generar_barcos(grid, cord, submarionos, cant_submarionos, dificultad, barcos, COLS, ROWS) #GENERA SUBMARINOS
    generar_barcos(grid, cord, destructors, cant_destructors, dificultad, barcos, COLS, ROWS) #GENERA DESTRUCTORES
    generar_barcos(grid, cord, cruceros, cant_cruceros, dificultad, barcos, COLS, ROWS) #GENERA CRUCEROS
    generar_barcos(grid, cord, acorazado, cant_acorazado, dificultad, barcos, COLS, ROWS) #GENERA ACORAZADOS
    return barcos



def verifica_espacio_libre(tam_barco, grid, col_inicio, fila):
        espacio_libre = True
        for i in range(tam_barco):
            if grid[fila + i][col_inicio] != 0:
                espacio_libre = False
                break
        return espacio_libre

def verificar_disparo_barco(x_y, barcos, grid, cord):
    impacto = False
    for barco in barcos:
        if x_y in barco['Cordenadas'] and barco['Vida'] > 0:
            print("¡El mouse está dentro de esta celda!")
            impacto = True
            for i in range(len(grid)):              #esto hace cambio el 1 del grid a 0 si toca la celda
                for x in range(len(grid[i])):
                    if cord[i][x] == x_y:
                        grid[i][x] = 0 
            barco['Vida'] -= 1
    return impacto

def verificar_disparo(cord, posi, celdas_ya_disparadas, barcos, CELLSIZE, grid):
    impacto = None
    for i in cord:
        for x_y in i: # cada celda es (x, y)
            rect = pg.Rect(x_y[0], x_y[1], CELLSIZE, CELLSIZE)
            if rect.collidepoint(posi):
                impacto = None
                if x_y not in celdas_ya_disparadas:
                    impacto = verificar_disparo_barco(x_y, barcos, grid, cord,)
                    celdas_ya_disparadas.append(x_y)
                elif x_y in celdas_ya_disparadas:
                    print('Ya disparaste')  
                    break
     
    return impacto

def verificar_vida_barcos(barcos):
    """
    Verifica si la partida ha terminado.
    Retorna True si todos los barcos han sido hundidos, False en caso contrario.
    """
    puntos = 0
    for barco in barcos:
        if barco['Vida'] <= 0:
            puntos += barco['Tam'] * 10
            barcos.remove(barco) 
    return puntos

def verificar_estado_partida(barcos):
    end = False
    if len(barcos) == 0:
        end = True
    return end
    
