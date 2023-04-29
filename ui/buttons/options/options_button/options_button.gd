extends TextureButton


const OPTIONS_MENU_PATH = "res://ui/buttons/options/options_menu/options_menu.tscn"


func _on_pressed():
	var parent = get_parent()
	var scene
	
	if parent.name == "Buttons": # TITLE SCREEN options button
		scene = parent.get_parent().get_parent()
	else:
		scene = parent.get_parent()
	
	var options_menu = preload(OPTIONS_MENU_PATH).instantiate()
	
	scene.add_child(options_menu)
