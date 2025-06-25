import pygame 
import settings as config
import pygame.mixer as mixer
from menu import *
from menu_levels import *
import game
import functions
from menu_score import *

# Inicializar Pygame
pygame.init()
mixer.init()
clock = pygame.time.Clock()

# Titulo 
pygame.display.set_caption("BATTLESHIP PRO MAX")

# Icono
pygame.display.set_icon(icon)

# Creando la ventana
screen_resolution = (config.SCREENWIDTH, config.SCREENHEIGHT)
screen = pygame.display.set_mode((screen_resolution))

# FONDO



dificult = 1
#FUENTE


# Bucle principal del juego-----------------------------------------------------------------------------
while True:
    clock.tick(83)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        opcion = menu()

        match opcion:
            case 1:
                dificult = menu_levels(screen, clock)
            case 2:
                functions.transicion_get_ready(screen)
                game.start(screen, dificult, config.CELLSIZE, config.ROWS, config.COLS)
            case 3:
                menu_score(screen)
        

    pygame.display.flip()