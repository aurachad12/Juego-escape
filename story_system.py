import pygame
import sys
# NUEVO: Importar el sistema de historia
from story_system import StoryManager

# Importar otros módulos de tu juego
try:
    from Valores import ANCHO_PANTALLA, ALTO_PANTALLA
    WIDTH, HEIGHT = ANCHO_PANTALLA, ALTO_PANTALLA
except ImportError:
    WIDTH, HEIGHT = 1280, 720

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tu Juego")
        self.clock = pygame.time.Clock()
        
        # NUEVO: Inicializar el sistema de historia
        self.story_manager = StoryManager(WIDTH, HEIGHT)
        
        # Variables del juego
        self.running = True
        self.game_started = False
        
        # Variables del jugador (tus variables existentes)
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.player_speed = 5
        
        # Variables de progreso del juego
        self.level = 1
        self.keys_collected = 0
        self.doors_opened = 0
        self.enemies_defeated = 0
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # NUEVO: Dejar que el story manager maneje la entrada primero
            story_handled = self.story_manager.handle_input(event)
            
            # Solo procesar otros controles si la historia no los manejó
            if not story_handled:
                self.handle_game_input(event)
    
    def handle_game_input(self, event):
        """Maneja la entrada específica del juego"""
        if event.type == pygame.KEYDOWN:
            # Tus controles existentes del juego
            keys = pygame.key.get_pressed()
            
            # Ejemplo de controles de movimiento
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player_x -= self.player_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player_x += self.player_speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.player_y -= self.player_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player_y += self.player_speed
    
    def update(self):
        # NUEVO: Actualizar el sistema de historia
        self.story_manager.update()
        
        # NUEVO: Si es la primera vez, mostrar la historia de inicio
        if not self.game_started:
            self.story_manager.trigger_story("intro")
            self.game_started = True
        
        # Aquí va tu lógica de actualización del juego
        self.update_game_logic()
    
    def update_game_logic(self):
        """Tu lógica de juego existente"""
        
        # Ejemplo: Detectar colisiones con llaves
        # if self.player_collides_with_key():
        #     self.collect_key()
        
        # Ejemplo: Detectar colisiones con puertas
        # if self.player_collides_with_door() and self.keys_collected > 0:
        #     self.open_door()
        
        # Ejemplo: Detectar colisiones con enemigos
        # if self.player_collides_with_enemy():
        #     self.fight_enemy()
        
        pass
    
    # NUEVO: Métodos para activar historias cuando sucedan eventos
    def collect_key(self):
        """Llamar cuando el jugador recoge una llave"""
        self.keys_collected += 1
        # Notificar al sistema de historia
        self.story_manager.update_progress(keys_found=1)
        print(f"¡Llave recogida! Total: {self.keys_collected}")
    
    def open_door(self):
        """Llamar cuando el jugador abre una puerta"""
        if self.keys_collected > 0:
            self.keys_collected -= 1
            self.doors_opened += 1
            # Notificar al sistema de historia
            self.story_manager.update_progress(doors_opened=1)
            print(f"¡Puerta abierta! Total: {self.doors_opened}")
    
    def defeat_enemy(self):
        """Llamar cuando el jugador derrota un enemigo"""
        self.enemies_defeated += 1
        # Notificar al sistema de historia
        self.story_manager.update_progress(enemies_defeated=1)
        print(f"¡Enemigo derrotado! Total: {self.enemies_defeated}")
    
    def advance_level(self):
        """Llamar cuando el jugador avanza de nivel"""
        self.level += 1
        # Notificar al sistema de historia
        self.story_manager.update_progress(level=self.level)
        print(f"¡Nivel {self.level}!")
    
    def draw(self):
        # Limpiar pantalla
        self.screen.fill((30, 30, 30))
        
        # AQUÍ VA TU CÓDIGO DE DIBUJO EXISTENTE
        self.draw_game()
        
        # NUEVO: Dibujar la historia (SIEMPRE AL FINAL para que aparezca encima)
        self.story_manager.draw(self.screen)
        
        pygame.display.flip()
    
    def draw_game(self):
        """Tu código de dibujo existente"""
        
        # Ejemplo: Dibujar jugador
        pygame.draw.rect(self.screen, (0, 255, 0), (self.player_x, self.player_y, 30, 30))
        
        # Ejemplo: Dibujar UI
        font = pygame.font.Font(None, 36)
        
        # Mostrar estadísticas
        stats = [
            f"Nivel: {self.level}",
            f"Llaves: {self.keys_collected}",
            f"Puertas abiertas: {self.doors_opened}",
            f"Enemigos derrotados: {self.enemies_defeated}"
        ]
        
        for i, stat in enumerate(stats):
            text = font.render(stat, True, (255, 255, 255))
            self.screen.blit(text, (10, 10 + i * 30))
        
        # Instrucciones temporales para probar
        instructions = [
            "PRUEBAS:",
            "K - Recoger llave",
            "D - Abrir puerta", 
            "E - Derrotar enemigo",
            "N - Siguiente nivel"
        ]
        
        for i, instruction in enumerate(instructions):
            text = font.render(instruction, True, (150, 150, 150))
            self.screen.blit(text, (WIDTH - 250, 10 + i * 25))
    
    def handle_test_keys(self, event):
        """Método temporal para probar el sistema"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:  # Simular recoger llave
                self.collect_key()
            elif event.key == pygame.K_d:  # Simular abrir puerta
                self.open_door()
            elif event.key == pygame.K_e:  # Simular derrotar enemigo
                self.defeat_enemy()
            elif event.key == pygame.K_n:  # Simular subir nivel
                self.advance_level()
    
    def run(self):
        while self.running:
            self.handle_events()
            
            # TEMPORAL: Para probar el sistema
            for event in pygame.event.get():
                self.handle_test_keys(event)
            
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# NUEVO: También puedes agregar historias personalizadas
def setup_custom_stories(story_manager):
    """Agregar historias específicas de tu juego"""
    # Crear directamente el StoryEvent aquí
    from story_system import StoryEvent
    
    # Historia personalizada
    custom_story = StoryEvent(
        story_id="custom_intro",
        title="Tu Historia Personalizada",
        messages=[
            "Este es tu mensaje personalizado...",
            "Puedes agregar tantos mensajes como quieras.",
            "¡Perfecto para tu juego específico!"
        ],
        trigger_condition="start"
    )
    
    story_manager.add_story_event(custom_story)

if __name__ == "__main__":
    game = Game()
    
    # NUEVO: Configurar historias personalizadas si las tienes
    # setup_custom_stories(game.story_manager)
    
    game.run()