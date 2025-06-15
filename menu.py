import pygame 
import random
import time
import pygame.mixer as mixer
from main import *
mixer.init()
clock = pygame.time.Clock()

# Inicializar Pygame
pygame.init()

# Titulo 
pygame.display.set_caption("BATTLESHIP PRO MAX")

# Icono
icon = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/icono.png")
pygame.display.set_icon(icon)

# Musica
muted = False
logo_sonidosi = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/sonidosi.png")
logo_sonidosi = pygame.transform.scale(logo_sonidosi, (40, 40))
logo_sonidono = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/sonidono.png")
logo_sonidono = pygame.transform.scale(logo_sonidono, (40, 40))
mixer.music.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/musicamenu.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)

# Creando la ventana
screen_resolution = (800, 600)
screen = pygame.display.set_mode((screen_resolution))

# FONDO
frame_actual = 0
N = 83
fondo_frames = []
for i in range(0, N+1):  # Empieza en 0
    num = str(i).zfill(2)  # '00', '01', ..., '83'
    frame = pygame.image.load(f"C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/frame_{num}_delay-0.05s.png")
    frame = pygame.transform.scale(frame, (800, 600))
    fondo_frames.append(frame)





#FUENTE
font = pygame.font.Font("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/Michroma.ttf", 50)


boton_start_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonstart.png")
boton_start_img = pygame.transform.scale(boton_start_img, (140, 60))
boton_start_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonstartanimado.png")
boton_start_hover_img = pygame.transform.scale(boton_start_hover_img, (140, 60))

boton_levels_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonlevels.png")
boton_levels_img = pygame.transform.scale(boton_levels_img, (140, 60))
boton_levels_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonlevelsanimado.png")
boton_levels_hover_img = pygame.transform.scale(boton_levels_hover_img, (140, 60))

boton_scores_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonscores.png")
boton_scores_img = pygame.transform.scale(boton_scores_img, (140, 60))
boton_scores_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonscoresanimado.png")
boton_scores_hover_img = pygame.transform.scale(boton_scores_hover_img, (140, 60))

boton_exit_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonexit.png")
boton_exit_img = pygame.transform.scale(boton_exit_img, (140, 60))
boton_exit_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonexitanimado.png")
boton_exit_hover_img = pygame.transform.scale(boton_exit_hover_img, (140, 60))

# Botones dificultad
boton_easy_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botoneasy.png")
boton_easy_img = pygame.transform.scale(boton_easy_img, (200, 60))
boton_easy_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botoneasyanimado.png")
boton_easy_hover_img = pygame.transform.scale(boton_easy_hover_img, (200, 60))

boton_medium_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonmedium.png")
boton_medium_img = pygame.transform.scale(boton_medium_img, (200, 60))
boton_medium_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonmediumanimado.png")
boton_medium_hover_img = pygame.transform.scale(boton_medium_hover_img, (200, 60))

boton_hard_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonhard.png")
boton_hard_img = pygame.transform.scale(boton_hard_img, (200, 60))
boton_hard_hover_img = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/botonhardanimado.png")
boton_hard_hover_img = pygame.transform.scale(boton_hard_hover_img, (200, 60))


#DIFICULTAD
def menu_levels():
    running = True
    while running:
        global frame_actual
        frame_actual = (frame_actual + 1) % len(fondo_frames)
        screen.blit(fondo_frames[frame_actual], (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse_pos[0] <= 500 and 180 <= mouse_pos[1] <= 240:
                    print("Easy selected")
                    running = False
                if 300 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 310:
                    print("Medium selected")
                    running = False
                if 300 <= mouse_pos[0] <= 500 and 320 <= mouse_pos[1] <= 380:
                    print("Hard selected")
                    running = False

        # Hover para cada botón de dificultad
        if 300 <= mouse_pos[0] <= 500 and 180 <= mouse_pos[1] <= 240:
            screen.blit(boton_easy_hover_img, (300, 180))
        else:
            screen.blit(boton_easy_img, (300, 180))

        if 300 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 310:
            screen.blit(boton_medium_hover_img, (300, 250))
        else:
            screen.blit(boton_medium_img, (300, 250))

        if 300 <= mouse_pos[0] <= 500 and 320 <= mouse_pos[1] <= 380:
            screen.blit(boton_hard_hover_img, (300, 320))
        else:
            screen.blit(boton_hard_img, (300, 320))

        pygame.display.flip()
        clock.tick(60)



#TRANSICION DE PLAY
def transicion_get_ready():
    fade = pygame.Surface((800, 600))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, 10):
        fade.set_alpha(alpha)
        frame = (frame_actual + 1) % len(fondo_frames)
        screen.blit(fondo_frames[frame], (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(20)
    # Mostrar mensaje "Get ready..."
    font = pygame.font.Font("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/Michroma.ttf", 50)
    text = font.render("Get ready...", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (200, 250))
    pygame.display.update()
    pygame.time.delay(1500)

    pygame.mixer.music.stop()
    pygame.mixer.music.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/musicajuego.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)











#FUNCION QUE DIBUJA LOS BOTONES
def draw_button(text, x, y, w, h, text_color, font_name, font_size, hover=False):
    oval_margin = 0  
    ellipse_surface = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.ellipse(
        ellipse_surface,
        (50, 50, 50), 
        (oval_margin, oval_margin, w - 2 * oval_margin, h - 2 * oval_margin)
    )

    if hover:
        pygame.draw.ellipse(
            ellipse_surface,
            (255, 255, 255, 80),  # Blanco semitransparente
            (oval_margin, oval_margin, w - 2 * oval_margin, h - 2 * oval_margin)
        )
    screen.blit(ellipse_surface, (x, y))
    # Fuente
    if font_name.lower() == "michroma":
        font = pygame.font.Font("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/Michroma.ttf", font_size)
    else:
        font = pygame.font.SysFont(font_name, font_size, bold=True)
    label = font.render(text, True, text_color)
    label_rect = label.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(label, label_rect)



# Bucle principal del juego-----------------------------------------------------------------------------
# ...carga de imágenes y otros assets arriba...

while True:
    clock.tick(83)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Botón Levels
            if 5 <= mouse_pos[0] <= 145 and 100 <= mouse_pos[1] <= 160:
                menu_levels()
            # Botón Play
            if 5 <= mouse_pos[0] <= 145 and 175 <= mouse_pos[1] <= 235:
                transicion_get_ready()
                jugar()  # Llama a la función jugar() de main.py
            # Botón Scores
            if 5 <= mouse_pos[0] <= 145 and 250 <= mouse_pos[1] <= 310:
                print("Scores presionado")
            # Botón Exit
            if 5 <= mouse_pos[0] <= 145 and 325 <= mouse_pos[1] <= 385:
                pygame.quit()
                exit()
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
        screen.blit(boton_levels_hover_img, (5, 100))
    else:
        screen.blit(boton_levels_img, (5, 100))

    if 5 <= mouse_pos[0] <= 145 and 175 <= mouse_pos[1] <= 235:
        screen.blit(boton_start_hover_img, (5, 175))
    else:
        screen.blit(boton_start_img, (5, 175))

    if 5 <= mouse_pos[0] <= 145 and 250 <= mouse_pos[1] <= 310:
        screen.blit(boton_scores_hover_img, (5, 250))
    else:
        screen.blit(boton_scores_img, (5, 250))

    if 5 <= mouse_pos[0] <= 145 and 325 <= mouse_pos[1] <= 385:
        screen.blit(boton_exit_hover_img, (5, 325))
    else:
        screen.blit(boton_exit_img, (5, 325))

    # Icono de sonido
    if muted:
        screen.blit(logo_sonidono, (0, 560))
    else:
        screen.blit(logo_sonidosi, (0, 560))

    pygame.display.flip()