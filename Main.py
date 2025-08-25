# Main.py
import time
from movimiento_jugador import principal
from intro import main_intro
from menu.menuzaso import menu

def main():
    
    #main_intro()   # Ejecuta la intro del juego
    time.sleep(1)  # Pausa breve entre la intro y el menu
    menu()         # Muestra el menú principal
    
    
    principal.ejecutar_juego()

if __name__ == "__main__":
    main()
    
