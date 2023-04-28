# IMPORTS
from control    import Control
from bugtong    import Bugtong

from .phase     import Phase


# CLASS
class MemoryPhase(Phase):
    # Attributes
    PROMPT = f"""
[Don't press Enter] to keep memorizing.
[Press Enter] to skip phase.
Type [G] to see bugtongs guide.

Input: """
    
    
    # Set-up
    def __init__(self, time):
        super().__init__(time)
    
    
    # Unique Methods
    @staticmethod
    def input_to_action(input) -> str:
        action = None
        
        match input:
            case 'g':       action = "guide"
            case '':        action = "skipped"
            case "time":    action = "time"
            case _:         action = "invalid"
            
        return action
    
    
    def show_guide():
        print(f"---BUGTONG GUIDE---\n")

        for bugtong in Bugtong.real_raws:
            print(" | ".join(bugtong))

        print()
    
    
    @classmethod
    def print_action(cls, action, phase):
        print(f"\nAction: {action.title()}!\n")
        
        if action == "guide":
            cls.show_guide()
        
        Control.enter_to_continue()
                