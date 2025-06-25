import pygame as pg
from BibliotecaDemy import *

def mostrar_top_scores(screen, scores):
    font = pg.font.SysFont(None, 48)
    y = 150
    top_scores = scores[:3]
    for i in range(len(top_scores)):
        nombre = top_scores[i][0]
        puntos = top_scores[i][1]
        texto = font.render(f"{i+1}. {nombre}: {puntos}", True, (255,255,255))
        screen.blit(texto, (200, y))
        y += 60


def menu_score(screen):
    run = True
    while run:
        background = pg.image.load('assets\playbackground.png').convert()
        background = pg.transform.scale(background, (820, 600))
        screen.blit(background, (0,0))
        scores = []
        with open('puntos.csv', 'r') as score:
            scores = leer_csv(score)
            scores.sort(key=lambda x: x[1], reverse=True)   
        mostrar_top_scores(screen, scores)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            posi = (0, 0)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posi = (event.pos)
                    #RESTAR
                    if 5 <= posi[0] <= 130 and 135 <= posi[1] <= 159:
                        with open('puntos.csv', 'w+'):
                            continue
                    #MENU
                    elif 5 <= posi[0] <= 130 and 165 <= posi[1] <= 189:
                        run = False
