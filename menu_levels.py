import pygame

def menu_levels(screen, clock):
    from assets import background, boton_easy_hover_img, boton_medium_hover_img, boton_easy_img, boton_medium_img, boton_hard_hover_img, boton_hard_img
    dificultad = 1
    running = True
    while running:
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse_pos[0] <= 500 and 180 <= mouse_pos[1] <= 240:
                    print("Easy selected")
                    dificultad = 1
                    running = False
                if 300 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 310:
                    print("Medium selected")
                    dificultad = 2
                    running = False
                if 300 <= mouse_pos[0] <= 500 and 320 <= mouse_pos[1] <= 380:
                    print("Hard selected")
                    dificultad = 4
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
    return dificultad

