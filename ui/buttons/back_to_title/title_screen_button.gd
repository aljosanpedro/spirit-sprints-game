extends Control


const TITLE_SCREEN_PATH = "res://ui/screens/title/title_screen.tscn"


func _on_pressed():
	SceneSwitcher.scene_index = 0
	get_tree().change_scene_to_file(TITLE_SCREEN_PATH)
