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

    # Botones (si no hay imagen, la clase mostrará un fallback)
    ruta_start = os.path.join(BASE_DIR, "assets", "start.png")
    ruta_exit = os.path.join(BASE_DIR, "assets", "exit_button.png")
    ruta_options = os.path.join(BASE_DIR, "assets", "options.png")

    start_button = Button(ruta_start, (500, 450), scale=2, text=None)
    exit_button = Button(ruta_exit, (700, 450), scale=0.8, text=None)
    options_button = Button(ruta_options, (1225, 40), scale=0.3, text=None)

    # Si prefieres texto además de (o en lugar de) imágenes:
    # start_button = Button(None, (500, 450), scale=1.2, text="START")
    # exit_button = Button(None, (700, 450), scale=1.0, text="EXIT")
    # options_button = Button(None, (1225, 40), scale=0.8, text="OPTIONS")

    while True:
        # 1) Tomamos todos los eventos del frame una sola vez
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2) Lógica de botones con "edge click"
        if start_button.is_clicked(events):
            print("Iniciar juego")
            return  # Aquí arrancaría tu juego

        if exit_button.is_clicked(events):
            pygame.quit()
            sys.exit()

        if options_button.is_clicked(events):
            # Antes de entrar a Ajustes, opcionalmente limpiar clicks “en curso”
            pygame.event.clear()
            settings_menu(window)  # Pantalla modal de Ajustes
            # Al volver, limpiamos la cola para que no se re-accionen clicks
            pygame.event.clear()

        # 3) Dibujar
        window.blit(fondo, (0, 0))

        start_button.update()
        exit_button.update()
        options_button.update()

        start_button.draw(window)
        exit_button.draw(window)
        options_button.draw(window)

        pygame.display.flip()
        clock.tick(60)

