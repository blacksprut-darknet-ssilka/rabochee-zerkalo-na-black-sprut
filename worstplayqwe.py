import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Экран чист 🧼 (как твои мысли после медитации)")

clear_screen()
