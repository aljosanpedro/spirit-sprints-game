extends Control


const PAUSE_SCREEN_PATH = "res://prog/scenes/ui/screens/pause_screen.tscn"


func _on_pressed():
	var scene = get_parent().get_parent()
	var pause_screen = preload(PAUSE_SCREEN_PATH).instantiate()
	
	scene.add_child(pause_screen)
