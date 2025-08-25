import pygame
import sys
import os
from .button import Button
from .settings import settings_menu  
def loading_screen(window):
    X, Y = window.get_size()
    clock = pygame.time.Clock()
    
    fondo = pygame.Surface((X, Y))
    fondo.fill((0, 0, 0))
    
    pixel_size = 8  
    bar_width = 600
    bar_height = 16  
    bar_x = (X - bar_width) // 2
    bar_y = Y // 2
    progress = 0
    max_progress = 100
    
    try:
        font = pygame.font.Font(None, 24)  
    except:
        font = pygame.font.SysFont("Courier New", 16)  
    
    while progress <= max_progress:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if progress < max_progress:
            progress += 1
        
        window.blit(fondo, (0, 0))
        
        if progress == max_progress:
            loading_text = font.render("CARGADO", True, (0, 255, 0))  
        else:
            loading_text = font.render("CARGANDO...", True, (255, 255, 255))
            
        text_rect = loading_text.get_rect(center=(X//2, bar_y - 40))
        window.blit(loading_text, text_rect)
        
        fill_pixels = int(bar_width * (progress / max_progress))
        
        pygame.draw.rect(window, (100, 100, 100), (bar_x - 2, bar_y - 2, bar_width + 4, bar_height + 4), 2)
        
        pygame.draw.rect(window, (40, 40, 40), (bar_x, bar_y, bar_width, bar_height))
        
        for x in range(0, fill_pixels, pixel_size):
            for y in range(0, bar_height, pixel_size):
                pygame.draw.rect(window, (0, 255, 0), (bar_x + x, bar_y + y, pixel_size, pixel_size))
        
        percent_text = font.render(f"{progress}%", True, (255, 255, 255))
        percent_rect = percent_text.get_rect(center=(X//2, bar_y + bar_height + 30))
        window.blit(percent_text, percent_rect)
        
        pygame.display.flip()
        clock.tick(60)  
    
    pygame.time.wait(500)  
    
    return True  
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
        fondo.fill((50, 50, 50))  

    ruta_start = os.path.join(BASE_DIR, "assets", "jugar2.1.png")
    ruta_exit = os.path.join(BASE_DIR, "assets", "exit_button.png")
    ruta_options = os.path.join(BASE_DIR, "assets", "options.png")

    start_button = Button(ruta_start, (475, 450), scale=1, text=None)
    exit_button = Button(ruta_exit, (700, 450), scale=0.8, text=None)
    options_button = Button(ruta_options, (1225, 40), scale=0.3, text=None)

   

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if start_button.is_clicked(events):
            print("Iniciar juego")
            loading_screen(window)  
            return  
        
        if exit_button.is_clicked(events):
            pygame.quit()
            sys.exit()

        if options_button.is_clicked(events):
            pygame.event.clear()
            settings_menu(window)  
            pygame.event.clear()

        window.blit(fondo, (0, 0))

        start_button.update()
        exit_button.update()
        options_button.update()

        start_button.draw(window)
        exit_button.draw(window)
        options_button.draw(window)

        pygame.display.flip()
        clock.tick(60)

