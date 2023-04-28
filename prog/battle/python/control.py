# Imports
from os import system


# Class
class Control:
    # METHODS
    # Terminal
    @staticmethod
    def enter_to_continue():
        while True:
            continue_input = input(f"Press [Enter] to continue.")
            
            if continue_input == "":
                break
        print()
        
    @staticmethod
    def clear_screen():
        system("cls")
     
        
    # Flow
    @staticmethod
    def print_phase(phase):
        Control.clear_screen()
        print(f"\n---{phase.upper()}---\n")
    
    @staticmethod
    def print_end(phase):
        print(f"---{phase.upper()} END---\n")
    
    @staticmethod
    def is_battle_done(characters) -> str:
        player, enemy = characters
        winner = ""
                
        if enemy.health == 0:
            winner = player.name
        elif player.health == 0:
            winner = enemy.name
        
        return winner
    