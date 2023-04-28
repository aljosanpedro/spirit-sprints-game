# Imports
from control        import Control

from phases.memory  import MemoryPhase
from phases.play    import PlayPhase
from phases.result  import Result

from bugtong        import Bugtong
from card           import Card

from character      import Character


# Constants
PLAYER_HEALTH = 50
ENEMY_HEALTH = 50

MEMORY_PHASE_TIME = 15
PLAY_PHASE_TIME = 5

DAMAGE_HEALTH = 5

# Main
def main():
    characters = battle_start()
    
    while True:
        winner = Control.is_battle_done(characters)
        if not winner == "":
            battle_end(winner)
            break
        
        bugtongs, cards, characters = round_start(characters)
        
        characters = memory_phase(cards, characters)
        bugtong, action, time = play_phase(bugtongs)
        
        round_results(bugtong, cards, action, characters, time)
        
    return


# Flow Functions
def battle_start() -> list:
    Control.print_phase("battle start")
    
    Bugtong.load_raws() # load real & fake bugtongs and their attributes
    
    player = Character("Rara", PLAYER_HEALTH, "idle")
    enemy = Character("Pina", ENEMY_HEALTH, "idle")
    
    Character.damage_health = DAMAGE_HEALTH

    return [player, enemy]


def round_start(characters) -> list:
    Control.print_phase("round start")
    
    Character.set_anim_both("casting", *characters)

    bugtongs = Bugtong.draw_for_round() # [player,enemy,fake]    
    
    cards = Card.load_from_bugtongs(bugtongs) # player & enemy Bugtong -> cards
    Card.set_face_up(cards, False)
    
    Control.enter_to_continue()
    
    memory_phase_vars = [bugtongs, cards, characters]
    return memory_phase_vars


def memory_phase(cards, characters) -> list:
    phase = "memory phase"
    Control.print_phase(phase)
    memory_phase = MemoryPhase(MEMORY_PHASE_TIME) # set time
        
    Card.set_face_up(cards, True)

    input, time = MemoryPhase.timer_input(memory_phase) # timer; [Enter] -> skip, [G] -> guide
    action = MemoryPhase.input_to_action(input)
    MemoryPhase.print_action(action, phase)
    
    Card.set_face_up(cards, False)
    
    Control.print_end(phase)
    Control.enter_to_continue()

    return characters


def play_phase(bugtongs) -> list:
    phase = "play phase"
    Control.print_phase(phase)
    play_phase = PlayPhase(PLAY_PHASE_TIME)
    
    bugtong = Bugtong.draw_reading(bugtongs)
    PlayPhase.read_first(bugtong)

    input, time = PlayPhase.timer_input(play_phase)
    action = PlayPhase.input_to_action(input)
    PlayPhase.read_second(bugtong)
    PlayPhase.print_action(action, phase)
    
    
    Control.print_end(phase)
    
    return [bugtong, action, time]


def round_results(bugtong, cards, action, characters, time):
    phase = "results phase"
    Control.print_phase(phase)
    
    result, owner = Result.judge(bugtong, cards, action)
    Card.set_face_up(cards, True)
    Result.print_results(bugtong, result, owner)
    
    Character.apply_results(action, result, time, *characters)
    
    Control.print_end(phase)
    Control.enter_to_continue()
    

def battle_end(winner):
    Control.print_end("battle")
    
    print(f"Winner: {winner}\n")


# Run
if __name__ == "__main__":
    main()
