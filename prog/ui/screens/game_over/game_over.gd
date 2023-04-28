extends Control



var play_again_path := ""
const QUIT_TO_TITLE_PATH = "res://prog/scenes/ui/title_screen.tscn"



func _on_play_again_pressed():
	var path := "" # shorter name for convenience
	
	match Global.current_battle:
		"galangmundo":
			path = "res://prog/scenes/battle/gm_battle.tscn"
		"puno":
			path = "res://prog/scenes/battle/puno_battle.tscn"
		"ilog":
			path = "res://prog/scenes/battle/puno_battle.tscn"

	play_again_path = path

	Global.switch_scene(play_again_path)


func _on_quit_to_title_pressed():
	Global.switch_scene(QUIT_TO_TITLE_PATH)
