# IMPORTS
from time           import time
from inputimeout    import inputimeout, TimeoutOccurred

from control        import Control

# CLASS
class Phase:
    # Attributes
    PROMPT = ""
    
    
    # Set-up
    def __init__(self, time):
        self.time = time
       
        
    # Shared Methods
    @classmethod
    def timer_input(cls, self) -> str:
        time_ratio = 0
        
        print(f"{self.time} seconds! [Counting down...]")
        
        try:
            start_time = time()
            input = inputimeout(prompt=cls.PROMPT, timeout=self.time)
            end_time = time()
            
            time_ratio = Phase.calc_time_ratio(self, start_time, end_time)
        except TimeoutOccurred:
            input = "time"
            
            time_ratio = 0
        
        input = input.strip().lower()
        
        return [input, time_ratio]


    def calc_time_ratio(self, start_time, end_time):
        time_elapsed = end_time - start_time
        time_left = self.time - time_elapsed
        time_ratio = time_left / self.time
        time_ratio = round(time_ratio, 1)
        
        return time_ratio

    @staticmethod
    def print_action(action, phase):
        print(f"\nAction: {action.title()}!\n")
        
        Control.enter_to_continue()
        Control.print_phase(phase)
        