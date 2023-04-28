extends Control



const START_GAME_PATH = "res://prog/scenes/story/intro_story.tscn"
const CREDITS_PATH = "res://prog/scenes/ui/title_screen/credits.tscn"
const OPTIONS_PATH = "res://prog/scenes/ui/title_screen/options.tscn"


func _on_start_game_pressed():
#	Global.switch_scene(START_GAME_PATH)
	SceneSwitcher.next_scene()


func _on_credits_pressed():
	pass


# options button handled by options_button.tscn


func _on_quit_game_pressed():
	get_tree().quit()
