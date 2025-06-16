import pygame 

import pygame.mixer as mixer

import assets

mixer.init()
clock = pygame.time.Clock()

# Inicializar Pygame
pygame.init()

# Titulo 
pygame.display.set_caption("BATTLESHIP PRO MAX")

# Icono
icon = pygame.image.load("assets\icono.png")
pygame.display.set_icon(icon)


# Creando la ventana
screen_resolution = (800, 600)
screen = pygame.display.set_mode((screen_resolution))



# Bucle principal del juego-----------------------------------------------------------------------------
# ...carga de imágenes y otros assets arriba...
def menu():
    #MUSICA
    muted = False
    logo_sonidosi = pygame.image.load("assets\sonidosi.png")
    logo_sonidosi = pygame.transform.scale(logo_sonidosi, (40, 40))
    logo_sonidono = pygame.image.load("assets\sonidono.png")
    logo_sonidono = pygame.transform.scale(logo_sonidono, (40, 40))
    mixer.music.load("assets\musicamenu.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.2)
    #FONDO
    frame_actual = 0
    N = 83
    fondo_frames = []
    for i in range(0, N+1):  # Empieza en 0
        num = str(i).zfill(2)  # '00', '01', ..., '83'
        frame = pygame.image.load(f"assets\Frame_{num}_delay-0.05s.png")
        frame = pygame.transform.scale(frame, (800, 600))
        fondo_frames.append(frame)
    
    opcion = None
    select = False

    while not select:
        clock.tick(83)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Botón Levels
                if 5 <= mouse_pos[0] <= 145 and 100 <= mouse_pos[1] <= 160:
                    opcion = 1
                    select = True
                # Botón Play
                if 5 <= mouse_pos[0] <= 145 and 175 <= mouse_pos[1] <= 235:
                    opcion = 2
                    select = True
                    #transicion_get_ready()
                    #jugar(screen, 1, config.CELLSIZE, config.ROWS, config.COLS)  # Llama a la función jugar() de main.py
                # Botón Scores
                if 5 <= mouse_pos[0] <= 145 and 250 <= mouse_pos[1] <= 310:
                    opcion = 3
                    select = True
                # Botón Exit
                if 5 <= mouse_pos[0] <= 145 and 325 <= mouse_pos[1] <= 385:
                    pygame.quit()
                    exit()
                    select = True
                # Botón sonido
                if 0 <= mouse_pos[0] <= 40 and 560 <= mouse_pos[1] <= 600:
                    muted = not muted
                    if muted:
                        mixer.music.set_volume(0)
                    else:
                        mixer.music.set_volume(0.2)

        frame_actual = (frame_actual + 1) % len(fondo_frames)
        screen.blit(fondo_frames[frame_actual], (0, 0))

        # Dibuja los botones con animación hover
        if 5 <= mouse_pos[0] <= 145 and 100 <= mouse_pos[1] <= 160:
            screen.blit(assets.boton_levels_hover_img, (5, 100))
        else:
            screen.blit(assets.boton_levels_img, (5, 100))

        if 5 <= mouse_pos[0] <= 145 and 175 <= mouse_pos[1] <= 235:
            screen.blit(assets.boton_start_hover_img, (5, 175))
        else:
            screen.blit(assets.boton_start_img, (5, 175))

        if 5 <= mouse_pos[0] <= 145 and 250 <= mouse_pos[1] <= 310:
            screen.blit(assets.boton_scores_hover_img, (5, 250))
        else:
            screen.blit(assets.boton_scores_img, (5, 250))

        if 5 <= mouse_pos[0] <= 145 and 325 <= mouse_pos[1] <= 385:
            screen.blit(assets.boton_exit_hover_img, (5, 325))
        else:
            screen.blit(assets.boton_exit_img, (5, 325))

        # Icono de sonido
        if muted:
            screen.blit(logo_sonidono, (0, 560))
        else:
            screen.blit(logo_sonidosi, (0, 560))
   
        pygame.display.flip()
    return opcion