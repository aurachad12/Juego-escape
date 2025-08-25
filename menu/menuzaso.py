import pygame
import sys
import os
from .button import Button
from .settings import settings_menu  # Importamos el menú de ajustes

def menu():
    """Función para mostrar el menú principal del juego."""
    pygame.init()

    X, Y = 1280, 720
    window = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Menú")

    clock = pygame.time.Clock()
    BASE_DIR = os.path.dirname(__file__)

    # Fondo
    ruta_fondo = os.path.join(BASE_DIR, "assets", "H2O.jpeg")
    if os.path.exists(ruta_fondo):
        fondo = pygame.image.load(ruta_fondo).convert()
        fondo = pygame.transform.scale(fondo, (X, Y))
    else:
        fondo = pygame.Surface((X, Y))
        fondo.fill((50, 50, 50))  # gris si no hay imagen

    # Rutas de imágenes
    ruta_start = os.path.join(BASE_DIR, "assets", "jugar2.1.png")
    ruta_exit = os.path.join(BASE_DIR, "assets", "salir.png")
    ruta_options_normal = os.path.join(BASE_DIR, "assets", "options.png")
    ruta_options_hover = os.path.join(BASE_DIR, "assets", "algo.png")  # <- imagen al hacer hover

    # Crear botones
    start_button = Button(ruta_start, (475, 450), scale=1, text=None)
    exit_button = Button(ruta_exit, (800, 450), scale=1, text=None)
    options_button = Button(ruta_options_normal, (1225, 40), scale=0.75, text=None)
    options_button1 = Button(ruta_options_hover, (1000, 40), scale=0.75, text=None)

    # Cargar imagen de hover como Surface
    img_options_normal = pygame.image.load(ruta_options_normal).convert_alpha()
    img_options_hover = pygame.image.load(ruta_options_hover).convert_alpha()

    # Estado de hover previo para evitar reinicios constantes
    hover_anterior = False

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if start_button.is_clicked(events):
            print("Iniciar juego")
            return

        if exit_button.is_clicked(events):
            pygame.quit()
            sys.exit()

        if options_button.is_clicked(events):
            pygame.event.clear()
            settings_menu(window)
            pygame.event.clear()

        # Detectar si el mouse está sobre options_button y cambiar imagen base
        if options_button.rect.collidepoint(pygame.mouse.get_pos()):
            if not hover_anterior:
                options_button.original_image = img_options_hover
                hover_anterior = True
        else:
            if hover_anterior:
                options_button.original_image = img_options_normal
                hover_anterior = False

        # Dibujar
        window.blit(fondo, (0, 0))

        start_button.update()
        exit_button.update()
        options_button.update()

        start_button.draw(window)
        exit_button.draw(window)
        options_button.draw(window)

        pygame.display.flip()
        clock.tick(60)