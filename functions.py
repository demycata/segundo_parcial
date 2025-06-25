
import pygame as pg 
import random

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    '''
    Función para inicializar una matriz con un valor inicial.
    Args:
        cantidad_filas: int: Cantidad de filas de la matriz.
        cantidad_columnas: int: Cantidad de columnas de la matriz.
        valor_inicial: str | int: Valor inicial con el que se llenará la matriz.
    Returns:
        list: Matriz inicializada con el valor inicial.
    '''
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list) -> None:
    """
    Función para mostrar una matriz en la consola.
    Args:
        matriz: list: Matriz a mostrar.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

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

def dibujar_Grilla(display, cellsize, grid, celdas_ya_disparadas, celdas_acertadas):
    """Dibuja solo la cuadrícula del jugador en la pantalla"""
    from assets import cell, agua, barco
    cell = pg.transform.scale(cell, (cellsize, cellsize))
    agua = pg.transform.scale(agua, (cellsize, cellsize))
    barco = pg.transform.scale(barco, (cellsize, cellsize))
    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos_x = start_x + j * cellsize
            pos_y = start_y + i * cellsize
            if (pos_x, pos_y) in celdas_acertadas: # ROJO si ya estan disparadas
                display.blit(barco, (pos_x, pos_y))
            elif (pos_x, pos_y) in celdas_ya_disparadas: # AZUL si ya estan disparadas
                display.blit(agua, (pos_x, pos_y))
            else:   # si no las pone en blanco
                display.blit(cell, (pos_x, pos_y))

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
    if dificultad == 4:
        dificultad = 3
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

def verificar_disparo_barco(x_y, barcos, grid, cord, celdas_acertadas):
    impacto = False
    for barco in barcos:
        if x_y in barco['Cordenadas'] and barco['Vida'] > 0:
            print("¡El mouse está dentro de esta celda!")
            celdas_acertadas.append(x_y)
            impacto = True
            for i in range(len(grid)):              #esto hace cambio el 1 del grid a 0 si toca la celda
                for x in range(len(grid[i])):
                    if cord[i][x] == x_y:
                        grid[i][x] = 0 
            barco['Vida'] -= 1
    return impacto

def verificar_disparo(cord, posi, celdas_ya_disparadas, barcos, CELLSIZE, grid, celdas_acertadas):
    impacto = None
    for i in cord:
        for x_y in i: # cada celda es (x, y)
            rect = pg.Rect(x_y[0], x_y[1], CELLSIZE, CELLSIZE)
            if rect.collidepoint(posi):
                impacto = None
                if x_y not in celdas_ya_disparadas:
                    impacto = verificar_disparo_barco(x_y, barcos, grid, cord, celdas_acertadas)
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
    
def transicion_get_ready(screen):
    from assets import background
    fade = pg.Surface((800, 600))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, 10):
        fade.set_alpha(alpha)
        screen.blit(background, (0, 0))
        screen.blit(fade, (0, 0))
        pg.display.update()
        pg.time.delay(20)
    # Mostrar mensaje "Get ready..."
    font = pg.font.Font("assets\Michroma.ttf", 50)
    text = font.render("Get ready...", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (200, 250))
    pg.display.update()
    pg.time.delay(1500)

    pg.mixer.music.stop()
    pg.mixer.music.load("assets\musicajuego.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.2)
    
def mostrar_puntos(puntos, display):
    fuente = pg.font.SysFont(None, 36)
    if puntos < 0:
        puntos = puntos * -1
        texto = fuente.render(f'-{puntos:04d}', True, (255, 255, 255))
    else:
        texto = fuente.render(f'{puntos:04d}', True, (255, 255, 255))
    display.blit(texto, (50, 70))



def guardar_score(screen, PUNTOS):
    name = ''
    font = pg.font.Font(None, 50)
    cuadro = pg.image.load('assets\cuadro.png')
    run = True
    while run:
        screen.blit(cuadro, (100, 0))
        text = font.render(f"{name}", True, (255, 255, 255))
        screen.blit(text, (200, 300))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    name = name[0:-1] 
                elif event.key == pg.K_RETURN:
                    run = False
                else:
                    name += event.unicode
        pg.display.flip()

    with open('puntos.csv', 'a') as score:
        score.write(f'{name},{PUNTOS}\n')
    return False