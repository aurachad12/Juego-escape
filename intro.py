import pygame
import sys
import math

def draw_loading_spinner(surface, center, radius, frame, alpha=255):
    """Dibuja una ruedita de carga optimizada"""
    # Parámetros de la animación
    rotation_speed = 6
    num_dots = 8
    
    for i in range(num_dots):
        # Calcular ángulo para cada punto
        angle = math.radians((frame * rotation_speed + i * (360 / num_dots)) % 360)
        
        # Calcular posición del punto
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))
        
        # Calcular alpha para efecto de desvanecimiento
        dot_alpha = max(50, int(alpha * (1 - i * 0.1)))
        
        # Calcular tamaño del punto
        dot_size = 4 if i == 0 else max(2, 4 - i // 2)
        
        # Color con alpha aplicado directamente
        color_value = int(255 * (dot_alpha / 255))
        color = (color_value, color_value, color_value)
        
        # Dibujar círculo directamente sin superficie temporal
        pygame.draw.circle(surface, color, (x, y), dot_size)

def main_intro():
    # Inicializar Pygame
    pygame.init()

    # Pantalla
    try:
        from Valores import ANCHO_PANTALLA, ALTO_PANTALLA
        WIDTH, HEIGHT = ANCHO_PANTALLA, ALTO_PANTALLA
    except ImportError:
        # Valores por defecto si no se encuentra el módulo
        WIDTH, HEIGHT = 1280, 720
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Palermo Studios Intro")

    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ACCENT_COLOR = (100, 149, 237)  # Un azul elegante para variación

    # Reloj
    clock = pygame.time.Clock()

    # Fuentes
    try:
        # Intentar usar fuentes más elegantes
        big_font = pygame.font.Font(None, 150)
        small_font = pygame.font.Font(None, 70)
    except:
        big_font = pygame.font.SysFont("Arial", 150, bold=True)
        small_font = pygame.font.SysFont("Arial", 70)

    # Renderizar textos una sola vez (optimización)
    logo_text = big_font.render("P", True, WHITE)
    studio_text = small_font.render("PALERMO STUDIOS", True, WHITE)
    
    # Pre-crear superficies con alpha para evitar recrearlas cada frame
    logo_surface = logo_text.convert_alpha()
    studio_surface = studio_text.convert_alpha()

    # Centrado mejorado
    logo_rect = logo_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    studio_rect = studio_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    
    # Posición de la ruedita de carga
    loading_center = (WIDTH // 2, HEIGHT - 100)
    loading_radius = 25

    # Parámetros de animación (en frames a 60 FPS) - 5 segundos total
    FADE_IN_FRAMES = 30      # 0.5 segundos
    HOLD_FRAMES = 30         # 0.5 segundos  
    FADE_OUT_FRAMES = 30     # 0.5 segundos
    STUDIO_FADE_IN_FRAMES = 30  # 0.5 segundos
    LOADING_FRAMES = 180        # 3 segundos de carga simulada
    
    logo_transition_end = FADE_IN_FRAMES + HOLD_FRAMES + FADE_OUT_FRAMES  # 1.5 segundos
    total_duration = logo_transition_end + STUDIO_FADE_IN_FRAMES + LOADING_FRAMES  # 5 segundos total

    frame = 0
    running = True
    
    while running:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Permitir salir con ESC o SPACE
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    running = False

        screen.fill(BLACK)

        # Animación del logo "P"
        if frame < logo_transition_end:
            if frame < FADE_IN_FRAMES:
                # Fade in
                alpha = int((frame / FADE_IN_FRAMES) * 255)
            elif frame < FADE_IN_FRAMES + HOLD_FRAMES:
                # Hold
                alpha = 255
            else:
                # Fade out
                fade_out_frame = frame - FADE_IN_FRAMES - HOLD_FRAMES
                alpha = max(0, int(255 * (1 - fade_out_frame / FADE_OUT_FRAMES)))
            
            # Crear superficie con alpha para mejor rendimiento
            logo_surface.set_alpha(alpha)
            screen.blit(logo_surface, logo_rect)

        # Animación del texto "PALERMO STUDIOS" y carga
        elif frame < total_duration:
            studio_frame = frame - logo_transition_end
            if studio_frame < STUDIO_FADE_IN_FRAMES:
                # Fade in del texto del estudio
                alpha = int((studio_frame / STUDIO_FADE_IN_FRAMES) * 255)
            else:
                # Texto completamente visible durante la carga
                alpha = 255
            
            studio_surface.set_alpha(alpha)
            screen.blit(studio_surface, studio_rect)
            
            # Ruedita de carga girando durante 3 segundos
            draw_loading_spinner(screen, loading_center, loading_radius, frame, alpha)

        # Actualizar pantalla
        pygame.display.flip()
        frame += 1
        clock.tick(60)

        # Terminar animación después del tiempo definido O con teclas
        if frame >= total_duration:
            running = False

    # Pequeña pausa antes de salir (reducida)
    pygame.time.wait(200)
    return

# Función adicional para testing
def test_intro():
    """Función para probar la intro de forma independiente"""
    main_intro()
    pygame.quit()

if __name__ == "__main__":
    test_intro()