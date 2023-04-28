# IMPORTS
# Built-in
from time       import sleep

# Files
from character  import Character

# Parent Class
from .phase     import Phase


# CLASS
class PlayPhase(Phase):
    # Attributes
    PROMPT = f"""
Type [A] to swipe left      [Defend] 
Type [D] to swipe right     [Attack]
[Enter] to do nothing       [Stand]

Input: """
    
    
    # Set-up
    def __init__(self, time):
        super().__init__(time)
    
    
    # Unique Methods
    @staticmethod
    def read_first(bugtong):
        reading = bugtong.first.upper()
        
        print("The announcer reads:")
        
        for _ in range(3):
            sleep(1)
            print("...")
        sleep(1)
        
        print(f"\n{reading}\n")
        
    @staticmethod
    def read_second(bugtong):
        second = bugtong.second.upper()
        answer = bugtong.answer.upper()
        
        print(f"\nThe announcer reads: \n\n{second}\n\n{answer}")
    
    @staticmethod
    def input_to_action(input) -> str:
        action = None
        
        match input:
            case 'd':       action = "attack"
            case 'a':       action = "counter"
            case '':        action = "stand"
            case 'time':    action = "time"
            case _:         action = "invalid"
                      
        return action
    