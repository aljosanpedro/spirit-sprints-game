extends Control



const START_GAME_PATH = "res://prog/scenes/story/intro_story.tscn"
const CREDITS_PATH = "res://ui/buttons/credits/credits_screen.tscn"
const OPTIONS_PATH = "res://ui/buttons/options/options_menu/options_menu.tscn"


func _on_start_game_pressed():
#	Global.switch_scene(START_GAME_PATH)
	SceneSwitcher.next_scene()


func _on_credits_pressed():
	var credits = preload(CREDITS_PATH).instantiate()
	add_child(credits)


# options button handled by options_button.tscn


func _on_quit_game_pressed():
	get_tree().quit()
