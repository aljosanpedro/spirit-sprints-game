extends Control


func _on_exit_menu_pressed():
	queue_free()


func _on_save_options_pressed():
	# get music & sound volume values -> apply

	queue_free()
